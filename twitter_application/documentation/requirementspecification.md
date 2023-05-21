# Requirements specification

## Purpose of the application

The application enables users to view, like and comment on already posted tweets. The user can also write their own tweets.  

## Users and mock data

- The application has regular users. 
- In order to enhance the user experience, the application does have mock data  (15 users, 30 tweets, 200 likes and 100 comments) 
  inserted to the database on initialization, in order to mimic a social network.
 - The mock data is retrieved from an external library [Mimesis](https://mimesis.name/en/master/index.html).

## UI draft

The application consists of four different views:

- login view 
- signup view 
- wall/dashboard
- view comments and write new comment

## Functionality offered by the basic version

### Before signing/ logging in
- user can register to application using usernname (unique, min 3 characters), password (min 6 characters) and name (min 2 characters)
- once registered, a user can login using username and password
- if the user does not exist, or the password does not match, the system will notify.

### After signing/logging in

#### WALL OF TWEETS/DASHBOARD
- the wall shows the users own tweets and tweets from other people.
- user can add tweets. 
- max 30 tweets are shown on the wall and tweets are ranked based on the newest tweet. 

#### TWEET, COMMENTING & LIKING
- each tweet shows the following information:
1) name of sender 
2) time of tweet sending 
3) message of tweet 
4) amount of likes
5) button to like tweet
6) button to view comments and write a new comment

- user can like tweets on their wall by clicking the like button by the tweet.
- same user can only like a tweet once. 
- user can comment on tweets in the *comment* - view, which opens when the the user pushes the *View comments* - button
- 10 newest comments are shown for each tweet.



