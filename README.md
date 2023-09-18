## **Spotify Recommender**

## Problem Statement
+ Create a music recommender system for Spotify based on data I pulled from my own playlists using the website below. From the data pulled, I then looked at the different features to choose which feature the system would be giving you recommendations off of. 
+ Data and feature explanation brought to you by plamere, http://organizeyourmusic.playlistmachinery.com/.

**Track Properties**

1.) Genre - the genre of the track

2.) Year - the release year of the recording. Note that due to vagaries of releases, re-releases, re-issues and general madness, sometimes the release years are not what you'd expect.

3.) Added - the earliest date you added the track to your collection.

4.) Beats Per Minute (BPM) - The tempo of the song.

5.) Energy - The energy of a song - the higher the value, the more energtic the song.

6.) Danceability - The higher the value, the easier it is to dance to this song.

7.) Loudness (dB) - The higher the value, the louder the song.

8.) Liveness - The higher the value, the more likely the song is a live recording.

9.) Valence - The higher the value, the more positive mood for the song.

10.) Length - The duration of the song.

11.) Acousticness - The higher the value the more acoustic the song is.

12.) Speechiness - The higher the value the more spoken word the song contains.

13.) Popularity - The higher the value the more popular the song is.

14.) Duration - The length of the song.

## Imports used in the notebooks.
+ Pandas
+ Numpy
+ Matplotlib
+ Sklearn

## Breakdown of Workbook.

The project is comprised of 3 main folders being code, images, and data.


***Code*** houses all the code done for the project which is broken up into 3 parts.
+ 1.) Cleaning and EDA houses all the data cleaning and exploratory data analysis I did to decide on my recommender metric.
+ 2.) Pre-processing and Modeling houses where I would look at the coefficients of the features and ran clustering models like Kmeans and DBSCAN for added insight.
+ 3.) Recommender houses the code used to build my final recommender system based off of the metric I chose, which was energy. This was then made into a streamlit app.

***Images*** folder holds the graphs I used for my presentation.

***Data*** folder contains all the playlists I gathered into csv's. 

## Overview and Conclusions

I gathered a bunch of playlists from Spotify focusing on different moods, but also added in some of the top tracks around the world. This is because, I wanted to see if different music attributes would then begin to cluster with the moods people were in and popularity. Looking further into the features, I decided energy would be the best fit and began to see if it would show distinct clusters. Running through the models and different iterations using the top correlated features, the clusters were never fully transparent and ended up having a lot of overlap. The only way to create more distinct clusters was by changing the features used in the models and using less features in them. This then showed more distinct clusters and started to give better insight into how moods can effect music composition as a whole. I then built the recommender system with the already scaled energy(1-100)to let people see regardless of genre, what playlist it would recommend them off current energy level. The system actually worked quite well but with more time I plan on editing the playlists used in the datasets to rely more on the moods instead of just adding popular songs.


