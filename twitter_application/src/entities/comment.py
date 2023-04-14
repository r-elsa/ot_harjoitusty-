import uuid


class Comment:
    def __init__(self, comment_id=None, user=None, tweet=None, send_time=None,  message=None):
        self.id = comment_id or str(uuid.uuid4())
        self.user = user
        self.tweet = tweet
        self.send_time = send_time
        self.message = message
