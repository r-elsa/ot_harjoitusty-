from entities.user import User
from entities.tweet import Tweet

class TweetService:
    def __init__(self, id=None):
        self.id = id
        self.tweets = []

    def create_tweet(self, id, user, send_time, message, picture_url, picture_textfield):
              
        self.tweets.append(Tweet(id, user, send_time, message, picture_url, picture_textfield))
        self.return_tweets()
     
    
    def return_tweets(self):
        for i in self.tweets:
            print(i.message)              
                  
                


    
 