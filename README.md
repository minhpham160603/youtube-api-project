# YouTube Channels Data Analysis

## Objective: 
 - Use YouTube's API v3 to query data of the favorite YouTube channels for data analysis.

## Data pre-process:
- Parse datetime in string format into pandas Timestamp, then to date name in week days.
- Transform 'duration' atribute from ISO_8601 into seconds (float).

## To analyze:
- Look up the most-viewed and least-viewed videos.
- Examine video upload schedules distribution for 7 days in the week.
- Analyze the correlation between comments and likes .vs views. 
- Draw a word cloud from all videos' titles.
- Visualize data with Seaborn, Matplotlib, and Natural Language Toolkit.

## To go further:
- Using machine learning model to predict the growth of the channels in the future.
- Analyze the tags to get audience's most interested topics for each channel.

Reference:
- The project is inspired by [this video](https://www.youtube.com/watch?v=D56_Cx36oGY&t=917s) of Thu Vu data analytics.
