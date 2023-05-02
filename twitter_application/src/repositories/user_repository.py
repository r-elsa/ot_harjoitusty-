
from db_connection import get_database_connection
from entities.user import User

class UserRepository:
    """_summary_
    """    
    def __init__(self, connection):
        """_summary_

        Args:
            connection (_type_): _description_
        """        
        self._connection = connection

    def find_all(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return [User(row["username"]) for row in rows]

user_repository = UserRepository(get_database_connection())
users = user_repository.find_all()
