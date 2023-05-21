from tkinter import Tk, ttk, W
from tkinter import *
from services.user_service import UserService
from services.tweet_service import TweetService
from services.like_service import LikeService
from services.comment_service import CommentService
from db_connection import get_db_connection
import uuid

class UI:
    """_summary_
    """
    def __init__(self, root):
        """_summary_

        Args:
            root (_type_): _description_
        """
        self._root = root
        self.login_error_variable = None
        self.register_error_variable = None
        self.tweet_error_variable = None
        self.login_error_variable = None
        self.userinstance  = None
        self.tweet_service= TweetService(get_db_connection())
        self.user_service =  UserService(get_db_connection())
        self.like_service = LikeService(get_db_connection())
        self.comment_service = CommentService(get_db_connection())
       
    from .dashboard_ui import show_dashboard, display_tweets
    from .register_ui import handle_register, show_register_page
    from .comment_view import show_comment_view, display_comments
    from .dashboard_events import comment_button_clicked,  like_button_clicked,  post_tweet
     
    def hide_current_view(self):
        """_summary_
        """
        list = self._root.grid_slaves()
        for l in list:
            l.destroy()
    
    def hide_current_grid(self):
        list = self._root.grid_slaves()
        for l in list:
            l.grid_forget()
    
    def handle_login(self, event=None):
        """_summary_

        Args:
            event (_type_, optional): _description_. Defaults to None.
        """  

        try: 
            username = self.username.get()
            password = self.password.get()
            if not (username and password):
                raise ValueError('Empty input field')
            
            successful_login, logged_in_user =  self.user_service.login(username, password) 
      
            if not successful_login:
                raise ValueError('wrong username or password')
            
            self.show_dashboard()
            self.display_tweets()
            self.userinstance= logged_in_user
        
        
        except ValueError as e:
            self.login_error_variable.set(e)
            self.login_error_label.grid(row =6, column =1)

            
    def show_login_page(self, event=None):
        """_summary_

        Args:
            event (_type_, optional): _description_. Defaults to None.
        """        
        self.hide_current_view()
        heading = ttk.Label(master=self._root, text="Login",
                            foreground="white",  background="black")
        heading.grid(row=0, column=0, columnspan=2, sticky=W)

        username = ttk.Label(master=self._root, text="Username")
        self.username = ttk.Entry(master=self._root)
        username.grid(row=3, column=0)
        self.username.grid(row=3, column=1)

        password = ttk.Label(master=self._root, text="Password")
        self.password = ttk.Entry(master=self._root)
        password.grid(row=5, column=0)
        self.password.grid(row=5, column=1)


        self.login_error_variable = StringVar()
        self.login_error_label = ttk.Label(
        master=self._root,
        textvariable=self.login_error_variable,
        foreground="red"
        )
        self.login_error_label.grid(row =501, column =1)

        login_button = ttk.Button(master=self._root, text="LOGIN")
        login_button.grid (row=7, column=1, columnspan=1)
        login_button.bind("<Button-1>", self.handle_login)
        
        register_button = ttk.Button(master=self._root, text="REGISTER")
        register_button.grid(row=7, column=0, columnspan=1)
        register_button.bind("<Button-1>", self.show_register_page)

    def start(self):
        """ Initializing function.
        """  
        self.show_login_page()




