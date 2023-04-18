import uuid


class Like:
    def __init__(self, like_id=None, user=None, tweet_id=None, send_time=None):
        self.id = like_id or str(uuid.uuid4())
        self.user = user
        self.tweet_id = tweet_id
        self.send_time = send_time
