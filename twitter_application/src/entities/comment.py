import uuid

class Comment:
    def __init__(self, comment_id=None, user_id=None, tweet_id=None, send_time=None,  message=None):
        """ This is the class that describes a comment

        Args:
            comment_id (string):  id of newly created comment
            user_id (string):  id of user who wrote comment
            tweet_id (string): id of tweet, to which comment belongs
            send_time (time): time that the comment was sent
            message (string): message of comment
        """
        self.comment_id = comment_id or str(uuid.uuid4())
        self.user_id = user_id
        self.tweet_id = tweet_id
        self.send_time = send_time
        self.message = message
