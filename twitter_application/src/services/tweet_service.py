import uuid
from entities.tweet import Tweet

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

    def create_tweet(self, id, user, send_time, message, picture_url):
        """ Post a new tweet

        Args:
            id (int)): id of Tweet 
            user (int): id of user who posted tweet
            send_time (date): date when tweet was posted
            message (string): content of tweet
            picture_url (string): url of picture added to tweet
        """        
        self.tweets.append(Tweet(id, user, send_time, message, picture_url ))

    def return_tweets(self):
        """ Return all tweets

        Returns:
            array: Array of tweet - objects.
        """  
        return self.tweets
