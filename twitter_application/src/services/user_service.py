from entities.user import User

class UserService:
    def __init__(self, id=None):
        self.id = id
        self.users = []

    def create_user(self, name, username, password):
              
        self.users.append(User(name, username, password, None, False))
        # check if user exists (username already exists)

    
    def return_users(self):
        for i in self.users:
            print(i.name, i.username, i.password)

    def login(self, username=None, password=None):
        user = None
        for i in self.users:
            if i.username == username:
                if i.password == password:
                    user = i
            
        
        return user
                    
        
        # check if username and password match

        # if match --> create user
        """ user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")
        self._user = user
        return user """
    
    def check_if_user_already_exists():
        pass
