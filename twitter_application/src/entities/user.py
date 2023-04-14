
class User:
    def __init__(self, name, username, password, profile_picture=None, admin=False):
        self.name = name
        self.username = username
        self.password = password
        self.profile_picture = profile_picture
        self.admin = admin
