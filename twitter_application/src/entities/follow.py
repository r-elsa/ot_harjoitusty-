import uuid


class Follow:
    """_summary_

    Args:
        comment_id (_type_, optional): _description_. Defaults to None.
        user (_type_, optional): _description_. Defaults to None.
        tweet_id (_type_, optional): _description_. Defaults to None.
        send_time (_type_, optional): _description_. Defaults to None.
        message (_type_, optional): _description_. Defaults to None.
    """  
    def __init__(self, follow_id=None, follower=None, following=None, send_time=None):
        """_summary_

    Args:
        comment_id (_type_, optional): _description_. Defaults to None.
        user (_type_, optional): _description_. Defaults to None.
        tweet_id (_type_, optional): _description_. Defaults to None.
        send_time (_type_, optional): _description_. Defaults to None.
        message (_type_, optional): _description_. Defaults to None.
    """  
        self.id = follow_id or str(uuid.uuid4())
        self.follower = follower
        self.following = following
        self.send_time = send_time
