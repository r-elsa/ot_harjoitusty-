# Architecture description

## Structure

The program follows a two-level layer architecture, as following:


```mermaid
 classDiagram
      UI -->  Services
      Entities -- Services
   
      class Services{
          class User Service
          class Tweet Service
          class Like Service
          class Comment service
      }
      class UI{
          class UI
      }
      class Entities {
      class User
      class Tweet
      class Like
      class comment
      }
    
```

## User Interface

The class UI hoolds the four different views:
- login
- register
- dashboard
- comment

The UI also does light application logic such as raising errors. The UserService, TweetService, LikeService and CommentService hold all the code that interact with the SQLite  database and render the data back to the UI.


## Sequence diagram 

### Creation of Tweet

After clicking "post tweet" the program continues as follows:

```mermaid
sequenceDiagram
  participant User
  participant UI
  participant TweetService
  participant tweet
  User->>UI: click "Post tweet"
  UI ->> TweetService: create_tweet(tweet_id, user_id, send_time, message, picture_url)
  TweetService ->> tweet: Tweet(tweet_id, user_id, send_time, message, picture_url)
  TweetService ->> Database: Tweet(tweet_id, user_id, send_time, message, picture_url)
  TweetService-->> UI: tweet 
  UI->> UI: display_tweets()

```

Adding Users, Likes and comments follow a very similar pattern. 

## Database 

The function *initialize_database* creates four tables
- User
- Tweet
- Like
- Comment










