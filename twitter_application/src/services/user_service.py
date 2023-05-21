from db_connection import get_db_connection
from entities.user import User


def get_user_by_row(row):
    return User(row[0], row[1], row[2], row[3], row[4]) if row else None

class UserService:
    """ Class, which logins, registers and returns users.
    """
    def __init__(self, connection):
         self.connection = connection

    def create_user(self, user_id, name, username, password, profile_picture, admin):
        """ Create a new user.

        Args:
            user_id (string):  id of user
            name (string):  full name of user 
            username (string):  username (nickname) of user 
            password(string): users' password
            profile_picture(string): url to profile picture 
            admin (boolean): whether the user is an admin or not
        """
        cursor = self.connection.cursor()

        cursor.execute(
            "select * from user where username = ?",
            (username,)
        )
        row = cursor.fetchone()

        if not row:
            new_user = User(user_id, name, username, password,
                            profile_picture, admin)
            cursor.execute(
                "insert into user (user_id, name, username, password,"\
                "profile_picture, admin) values (?, ?, ?, ?, ?, ?)",
                (new_user.user_id, new_user.name, new_user.username,
                 new_user.password, new_user.profile_picture, new_user.admin,)
            )
            return (True, new_user)
        return (False, None)

    def login(self, username, password):
        """ User login using username and password

        Args:
            username (string): Username.
            password (string): Password.

        Returns:
            tuple (boolean, User object) : if user exists -> True, otherwise False
        """
        cursor = self.connection.cursor()
        cursor.execute(
            "select * from user where username = ? and password = ?",
            (username, password)
        )
        row = cursor.fetchall()

        if row:
            user = list(map(get_user_by_row, row))[0]
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


user_service = UserService(get_db_connection())
