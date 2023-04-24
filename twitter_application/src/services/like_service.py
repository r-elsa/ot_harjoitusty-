import uuid
import time
from entities.like import Like

class LikeService:
    def __init__(self):
        self.id = uuid.uuid4
        self.likes = []

    def like(self,tweet_id):
        new_like = Like(uuid.uuid4(),"userid", tweet_id, time.time())
        print(tweet_id)
        self.likes.append(new_like)

    def return_likes(self):
        return self.likes

