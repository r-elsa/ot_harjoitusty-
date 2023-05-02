import uuid
from entities.user import User

class UserService:
    """ Class, which adds and returns users.

    Args:
        id (int): Id of User. 
        users (array): Array of Users.
      
    """     
    def __init__(self):
        """ The contructor of the class UserService

        Args:
            id (int): Id of User. 
            users (array): Array of Users.
            
        """ 
                 
        self.id = uuid.uuid4
        self.users = []

    def create_user(self, name, username, password):
        """ Create a new user.

        Args:
            name (string): name of user
            username (string): username of user
            password (string): password
        """        
        self.users.append(User(name, username, password, None, False))

    def return_users(self):
        """

        Returns:
            array: Array of User - objects
        """        
        return self.users

    def count_users(self):
        """ Count the amount of users

        Returns:
            int: amount of users
        """        
        return len(self.users)

    def login(self, username=None, password=None):
        """ Login user using username and password

        Args:
            username (string): Username.
            password (password): Password.

        Returns:
            object: User - object
        """        
        user = None
        for i in self.users:
            if i.username == username:
                if i.password == password:
                    user = i
        return user
