import uuid
import time

from entities.comment import Comment

class CommentService:
    def __init__(self):
        self.id = uuid.uuid4
        self.comments = []

    def comment(self,tweet_id):
        new_comment = Comment(uuid.uuid4(),"userid", tweet_id, time.time(), "mesage")
        print(tweet_id)
        self.comments.append(new_comment)

    def return_comments(self):
        return self.comments


    
