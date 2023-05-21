
import uuid

class User:
    def __init__(self, user_id, name, username, password, profile_picture=None, admin=False):
        """ This is the class that describes a user

        Args:
            user_id (string):  id of user
            name (string):  full name of user 
            username (string):  username (nickname) of user 
            password(string): users' password
            profile_picture(string): url to profile picture 
            admin (boolean): whether the user is an admin or not
          
        """
        self.user_id = user_id or str(uuid.uuid4())
        self.name = name
        self.username = username
        self.password = password
        self.profile_picture = profile_picture
        self.admin = admin
