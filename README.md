# Recommendation-System
## An aproach towards Content Based Recommendation System

In order to make the Recommendation System, there has to some data in Data Base which can be used to play Recommended videos.  

Collecting data and then uploading into database manually was boring and tiredsome. So I tried to automate this task.  

```this is an interactive approach towards recommendation System, so I decided to go with Movie Trailers```

First, I downloaded the movie trailers

To download the videos, ***'video_downloader.py'*** file is used.  

Then to provide thumbnails to the videos, I downloaded the movie posters using ***'movie_poster_downloader.py'*** file.  

And finally, video upload is done using ***'video_uploader.py'*** which is actually web automation technique to automatically upload the Data.  

## Screenshots
![Image](https://github.com/shubhamjain31/Recommendation-System/blob/master/ScreenShots/One.png)
![Image](https://github.com/shubhamjain31/Recommendation-System/blob/master/ScreenShots/Video%20Play%20Page.png)  

In the above picture, when we clicked on Half Girlfriend movie, the top two recommendations are of Manmarziyaan and Luka Chupi, which pretty much are related to each other(based on content).  

You can even use voice input to search for the video
