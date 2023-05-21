from db_connection import get_database_connection

class UserRepository:
    """_summary_
    """

    def __init__(self, connection):
        """_summary_

        Args:
            connection (_type_): _description_
        """
        self._connection = connection

user_repository = UserRepository(get_database_connection())
