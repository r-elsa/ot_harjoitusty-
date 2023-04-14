import uuid


class Tweet:
    def __init__(self, tweet_id=None, user=None, send_time=None, message=None, picture_url=None, picture_textfield=None):
        self.id = tweet_id or str(uuid.uuid4())
        self.user = user
        self.send_time = send_time
        self.message = message
        self.picture_url = picture_url
        self.picture_textfield = picture_textfield
