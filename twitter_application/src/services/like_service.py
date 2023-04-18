from entities.user import User
from entities.tweet import Tweet



class LikeService:
    def __init__(self, id):
        self.id = id
        
    def like(self,tweet_id):
        print(tweet_id)
