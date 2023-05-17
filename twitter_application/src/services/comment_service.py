import uuid
import time
from entities.comment import Comment
from db_connection import get_db_connection

class CommentService:
    """Class, which adds and returns comments.  

    Attributes:
        id: id of CommentService.
        comments: Comments of Tweets.
    """
    
    def __init__(self, connection):
        """ The constructor of the class, which creates a new instance of CommentService.
        """   
        self.connection = connection      
        self.comments = []

    def comment(self,tweet_id):
        """ Function to add a comment.

        Args:
            tweet_id (int): Id of the tweet to which the comment belongs.
        """        
        new_comment = Comment(str(uuid.uuid4()),"userid", tweet_id, time.time(), "message")

        cursor = self.connection.cursor()
        cursor.execute(
            "insert into comment (id, user_id, tweet_id, send_time, message) values (?, ?, ?, ?, ?)",

            (new_comment.id,new_comment.user_id, new_comment.tweet_id, new_comment.send_time, new_comment.message,)
        )

        self.connection.commit()
        self.comments.append(new_comment)

    def return_comments(self):
        """ Function to return all comments. 

        Returns:
            array: comment - objects
        """        
        return self.comments

comment_service = CommentService(get_db_connection())