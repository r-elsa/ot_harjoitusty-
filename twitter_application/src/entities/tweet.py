import uuid

class Tweet:
    def __init__(self, tweet_id=None, user_id=None, send_time=None,
                 message=None, picture_url=None):
        """ This is the class that describes a tweet

        Args:
            tweet_id (string):  id of newly created tweet
            user_id (string):  id of user who wrote tweet
            send_time (time): time that the tweet was sent
            message (string): message of tweet
            oicture_url (string): url of picture to tweet 

        """
        self.tweet_id = tweet_id or str(uuid.uuid4())
        self.user_id = user_id
        self.send_time = send_time
        self.message = message
        self.picture_url = picture_url
