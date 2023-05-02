import uuid


class Comment:
    """_summary_

        Args:
            comment_id (_type_, optional): _description_. Defaults to None.
            user (_type_, optional): _description_. Defaults to None.
            tweet_id (_type_, optional): _description_. Defaults to None.
            send_time (_type_, optional): _description_. Defaults to None.
            message (_type_, optional): _description_. Defaults to None.
    """  
      
    def __init__(self, comment_id=None, user=None, tweet_id=None, send_time=None,  message=None):
        """_summary_

        Args:
            comment_id (_type_, optional): _description_. Defaults to None.
            user (_type_, optional): _description_. Defaults to None.
            tweet_id (_type_, optional): _description_. Defaults to None.
            send_time (_type_, optional): _description_. Defaults to None.
            message (_type_, optional): _description_. Defaults to None.
        """        
        self.id = comment_id or str(uuid.uuid4())
        self.user = user
        self.tweet_id = tweet_id
        self.send_time = send_time
        self.message = message
