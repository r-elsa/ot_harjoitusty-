import uuid
import time
from entities.like import Like

class LikeService:
    """ Class, which adds and returns likes.

    Args:
        id (int): Id of Like. 
        likes(array): Array of Likes.
      
    """  
    def __init__(self):
        """ The contructor of the class LikeService

        Args:
            id (int): Id of Like. 
            likes(array): Array of Likes.
            
        """  
        self.id = uuid.uuid4
        self.likes = []

    def like(self,tweet_id):
        """ Add a like

        Args:
            tweet_id (int): Id of the tweet that is being liked. 
        """        
        new_like = Like(uuid.uuid4(),"userid", tweet_id, time.time())
        print(tweet_id)
        self.likes.append(new_like)

    def return_likes(self):
        """ Return all likes.

        Returns:
            array: Array of like - objects.
        """        
        return self.likes
