import uuid
import time
from entities.like import Like
from db_connection import get_db_connection

class LikeService:
    """ Class, which adds and returns likes.

    Args:
        id (int): Id of Like. 
        likes(array): Array of Likes.
      
    """  
    
    def __init__(self, connection):
        """ The contructor of the class LikeService

        Args:
            id (int): Id of Like. 
            likes(array): Array of Likes.
            
        """  
        self.likes = []
        self.connection = connection

    def like(self,tweet_id):
        """ Add a like

        Args:
            tweet_id (int): Id of the tweet that is being liked. 
        """        
        new_like = Like(str(uuid.uuid4()),"userid", tweet_id, time.time())
        
        cursor = self.connection.cursor()
        cursor.execute(
            "insert into like (id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            (new_like.id,new_like.user_id, new_like.tweet_id, new_like.send_time)
        )

        self.connection.commit()
        self.likes.append(new_like)
        return True


    def return_likes(self):
        """ Return all likes.

        Returns:
            array: Array of like - objects.
        """        
        return self.likes
    

like_service = LikeService(get_db_connection())    