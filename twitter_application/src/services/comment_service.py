import uuid
import time

from entities.comment import Comment

class CommentService:
    """Class, which adds and returns comments.  

    Attributes:
        id: id of CommentService.
        comments: Comments of Tweets.
    """
    def __init__(self):
        """ The constructor of the class, which creates a new instance of CommentService.
        """         
        self.id = uuid.uuid4
        self.comments = []

    def comment(self,tweet_id):
        """ Function to add a comment.

        Args:
            tweet_id (int): Id of the tweet to which the comment belongs.
        """        
        new_comment = Comment(uuid.uuid4(),"userid", tweet_id, time.time(), "message")
        self.comments.append(new_comment)

    def return_comments(self):
        """ Function to return all comments. 

        Returns:
            array: comment - objects
        """        
        return self.comments
