import uuid
from entities.user import User
from db_connection import get_db_connection
""" from faker import Faker """


def get_user_by_row(row):
        return User(row[0],row[1], row[2], row[3], row[4]) if row else None


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
                 
        self.connection = connection
        """ self.fake_instance = None """

    def create_user(self, id, name, username, password, profile_picture, admin):
        """ Create a new user.

        Args:
            name (string): name of user
            username (string): username of user
            password (string): password
        """

        cursor = self.connection.cursor()

        cursor.execute(
            "select * from user where username = ?",
            (username,)
        )
        row = cursor.fetchone()
        
        if not row: 
            new_user = User(id, name, username, password, profile_picture, admin)
            cursor.execute(
            "insert into user (id, name, username, password, profile_picture, admin) values (?, ?, ?, ?, ?, ?)",
            (new_user.id, new_user.name, new_user.username, new_user.password, new_user.profile_picture, new_user.admin,)
        )
            return (True, new_user)
        return (False, None)
        
        
    def login(self, username, password):
        """ Login user using username and password

        Args:
            username (string): Username.
            password (password): Password.

        Returns:
            object: User - object
        """ 
       
            
        cursor = self.connection.cursor()
        cursor.execute(
            "select * from user where username = ? and password = ?",
            (username,password)
        )
        row = cursor.fetchall()
          
        if row:  
            user = list(map(get_user_by_row,row))[0]
            return (True, user)
        return (False, None)


  
    def return_users(self):
        """

        Returns:
            array: Array of User - objects
        """  

        cursor = self.connection.cursor()
        cursor.execute("select * from user")
        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))


    """ def insert_fake_users(self):
               
        self.fake_instance = Faker()    


        username = self.fake_instance.name().strip(' ').lower()
        print(username)
        
    
        fake_user = User(str(uuid.uuid4()), "testname" "testusername", "testpwd", "url", False)

        cursor = self.connection.cursor()
        cursor.execute(
            "insert into user (id, name, username, password, profile_picture, admin) values (?, ?, ?, ?, ?, ?)",
            (fake_user.id, fake_user.name, fake_user.username, fake_user.password, fake_user.profile_picture, fake_user.admin)
        )

        self.connection.commit()  """


user_service = UserService(get_db_connection())



