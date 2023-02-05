import pandas

def find_channel_by_user_name(youtube, user):
        resp = youtube.channels().list(
            forUsername = user,
            part = 'id',
            fields = 'items(id)',
            maxResults = 1
        ).execute()

        # stev: 'items' may be absent
        items = resp.get('items', [])
        assert len(items) <= 1

        for item in items:
            assert item['id'] is not None
            return item['id']

        return None
    
def get_channel_stats(youtube, channel_ids):
    all_data = []
    
    request = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    id= channel_ids)
    
    response = request.execute()
    
    for item in response["items"]:
        data = {'channelName': item['snippet']['title'], 
               'subscribers': item['statistics']['subscriberCount'],
                'totalViews': item['statistics']['viewCount'],
                'totalVideos': item['statistics']['videoCount'],
                'playlistId': item['contentDetails']['relatedPlaylists']['uploads']
               }
        
        all_data.append(data)
        
    return pandas.DataFrame(all_data)

def get_video_from_playlist(youtube, playlist_id):
    video_ids = []
    request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50
        )
    response = request.execute()
    for item in response['items']:
        video_ids.append(item['contentDetails']['videoId'])
        
    next_page_token = response.get('nextPageToken')
    while next_page_token:
        # print(next_page_token, len(video_ids))
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken = next_page_token
        )
        response = request.execute()
        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])
        next_page_token = response.get('nextPageToken')
    return video_ids

def get_all_videos_info(youtube, video_ids):
    all_videos_info = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute()

        for video in response['items']:
            stats = {'snippet': ['channelTitle', 'title', 'description', 'tags', 'publishedAt'],
                     'statistics': ['viewCount', 'likeCount', 'commentCount'],
                     'contentDetails': ['duration', 'definition']}
            video_info = {}
            video_info = {'video_id': video['id']}

            for k in stats.keys():
                for v in stats[k]:
                    try:
                        video_info[v] = video[k][v]
                    except:
                        video_info[v] = None
            all_videos_info.append(video_info)
            
    return pandas.DataFrame(all_videos_info)
    