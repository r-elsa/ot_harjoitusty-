import uuid
from entities.user import User
from db_connection import get_db_connection




class UserService:
    """ Class, which adds and returns users.

    Args:
        id (int): Id of User. 
        users (array): Array of Users.
      
    """     
    def __init__(self, connection):
        """ The contructor of the class UserService

        Args:
            id (int): Id of User. 
            users (array): Array of Users.
            
        """ 
                 
        self.id = uuid.uuid4
        self.users = []

    def create_user(self, id, name, username, password, profile_picture, admin):
        """ Create a new user.

        Args:
            name (string): name of user
            username (string): username of user
            password (string): password
        """

    

        new_user = User(id,name, username, password, profile_picture, admin)
        
        cursor = self.connection.cursor()
        cursor.execute(
            "insert into user (id, name, username, password, profile_picture, admin) values (?, ?, ?, ?, ?, ?)",
            (new_user.id, new_user.name, new_user.username, new_user.password, new_user.profile_picture, new_user.admin)
        )

        self.connection.commit()

        self.users.append(User(id, name, username, password, None, False))

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

user_service = UserService(get_db_connection())