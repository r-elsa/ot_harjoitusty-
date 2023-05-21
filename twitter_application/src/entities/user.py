
import uuid

class User:
    """_summary_

    Args:
        comment_id (_type_, optional): _description_. Defaults to None.
        user (_type_, optional): _description_. Defaults to None.
        tweet_id (_type_, optional): _description_. Defaults to None.
        send_time (_type_, optional): _description_. Defaults to None.
        message (_type_, optional): _description_. Defaults to None.
    """

    def __init__(self, user_id, name, username, password, profile_picture=None, admin=False):
        """_summary_

        Args:
            comment_id (_type_, optional): _description_. Defaults to None.
            user (_type_, optional): _description_. Defaults to None.
            tweet_id (_type_, optional): _description_. Defaults to None.
            send_time (_type_, optional): _description_. Defaults to None.
            message (_type_, optional): _description_. Defaults to None.
        """
        self.user_id = user_id or str(uuid.uuid4())
        self.name = name
        self.username = username
        self.password = password
        self.profile_picture = profile_picture
        self.admin = admin
