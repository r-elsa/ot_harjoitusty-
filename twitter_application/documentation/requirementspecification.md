# Requirements specification

## Purpose of the application

The application enables users to view, like and comment tweets from people that they follow, and to write their own tweets.  

## Users

The application has regular users. An admin user with increased rights will be added if time allows (see further development ideas).

## UI draft

The application consists of four different views:

- login view
- signup view
- wall
- creation of new tweet

## Functionality offered by the basic version

### Before signing/ logging in
- user can register to application using usernname (unique, min 3 characters), password (min 6 characters) and name (min 2 characters)
- once registered, user can login using username and password
- if the user does not exist, or the password does not match, the system will notify.

### After signing/logging in

#### USER:
- user can add profile picture.

#### WALL OF TWEETS 
- every user has their own 'wall' where their name and profile picture is shown. 
- wall shows their own tweets and tweets from people that user follows.
- user can add tweets.
- max 15 tweets are shown on the wall and tweets are ranked based on the newest tweet. 

#### TWEET, COMMENTING & LIKING
- each tweet shows the following information:
1) name of sender
2) time of tweet sending
3) message of tweet
4) possibily a picture and a text field (optional)

- user can comment on tweets on their own wall (in the comment field of each picture).
- 5 newest comments are shown for each tweet.
- user can like tweets on their wall. (by clicking like button by the tweet).
- same user can only like tweet once. 


#### FOLLOWING AND FOLLOWERS
- user can search other users based on their name
- user can follow other people (following)
- user can unfollow other people
- user can see their amount of followers


## Further development ideas
- user can view individual followers and see when they started following.
- user can reject an individual follower.
- user can view tweets based on trending topics (all tweets, not only from people that the user follows. an additional category dropdown will be added to each tweet, which enables filtering by subject).
- admin with priviledged rights.


