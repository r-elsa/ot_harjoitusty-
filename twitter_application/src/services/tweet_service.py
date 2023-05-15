import uuid
from entities.tweet import Tweet
import time

class TweetService:
    """ Class, which adds and returns tweets.

    Args:
        id (int): Id of Tweet. 
        tweets (array): Array of Tweets.
      
    """  
    def __init__(self):
        """ The contructor of the class TweetService

        Args:
            id (int): Id of Tweet. 
            tweets (array): Array of Tweets.
            
        """  
        self.id = uuid.uuid4
        self.tweets = []
        self.connection = "grg"

    def create_tweet(self, id, user_id, send_time, message, picture_url):
        """ Post a new tweet

        Args:
            id (int)): id of Tweet 
            user (int): id of user who posted tweet
            send_time (date): date when tweet was posted
            message (string): content of tweet
            picture_url (string): url of picture added to tweet
        """     


        new_tweet = Tweet(id, user_id, send_time, message, picture_url)
        
        cursor = self.connection.cursor()
        cursor.execute(
            "insert into like (id, user_id, send_time, message, picture_url) values (?, ?, ?, ?, ?)",
            (new_tweet.id, new_tweet.user_id, new_tweet.send_time, new_tweet.message, new_tweet.picture_url)
        )

        self.connection.commit()

        self.tweets.append(new_tweet)

    def return_tweets(self):
        """ Return all tweets

        Returns:
            array: Array of tweet - objects.
        """  
        return self.tweets
