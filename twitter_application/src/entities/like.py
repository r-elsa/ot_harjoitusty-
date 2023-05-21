import uuid

class Like:
     def __init__(self, like_id=None, user_id=None, tweet_id=None, send_time=None):
        """ This is the class that describes a like
        Args:
            id (string):  id of new like
            user_id (string):  id of user who liked
            tweet_id (string): id of tweet, to which like belongs
            send_time (time): time that the tweet was liked
        """
        self.id = like_id or str(uuid.uuid4())
        self.user_id = user_id
        self.tweet_id = tweet_id
        self.send_time = send_time
