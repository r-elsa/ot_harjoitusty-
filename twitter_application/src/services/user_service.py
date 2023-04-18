from entities.user import User

class UserService:
    def __init__(self, id=None):
        self.id = id
        self.users = []

    def create_user(self, name, username, password):        
        self.users.append(User(name, username, password, None, False))
      

    
    def return_users(self):
        return self.users

    def count_users(self):
        return len(self.users)
     

    def login(self, username=None, password=None):
        user = None
        for i in self.users:
            if i.username == username:
                if i.password == password:
                    user = i
             
        return user
                    
        
    
    def check_if_user_already_exists():
        pass
