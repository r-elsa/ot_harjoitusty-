from tkinter import Tk, ttk, W
from tkinter import *
from services.user_service import UserService
from services.tweet_service import TweetService
from services.like_service import LikeService
from services.comment_service import CommentService
from db_connection import get_db_connection
import time
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
        self._current_view = None
        self.userinstance  = None
        self.tweet_service= TweetService(get_db_connection())
        self.user_service =  UserService(get_db_connection())
        self.like_service = LikeService(get_db_connection())
        self.comment_service = CommentService(get_db_connection())
  
    
    from .dashboard_ui import show_dashboard,post_tweet, display_tweets
    from .register_ui import handle_register, show_register_page


          
    def hide_current_view(self):
        """_summary_
        """
        list = self._root.grid_slaves()
        for l in list:
            l.destroy()
    

    def handle_login(self, event=None):
        """_summary_

        Args:
            event (_type_, optional): _description_. Defaults to None.
        """        
        username = self.username.get()
        password = self.password.get()
  
        successful_login, logged_in_user =  self.user_service.login(username, password) 

        if successful_login:
            self.show_dashboard()
            self.display_tweets()
            self.userinstance= logged_in_user
            


    def show_login_page(self, event=None):
        """_summary_

        Args:
            event (_type_, optional): _description_. Defaults to None.
        """        
        self.hide_current_view()
        heading = ttk.Label(master=self._root, text="Login",
                            foreground="white",  background="black")

        username = ttk.Label(master=self._root, text="Username")
        self.username = ttk.Entry(master=self._root)

        password = ttk.Label(master=self._root, text="Password")
        self.password = ttk.Entry(master=self._root)

        login_button = ttk.Button(master=self._root, text="LOGIN")
        register_button = ttk.Button(master=self._root, text="REGISTER")
        heading.grid(row=0, column=0, columnspan=2, sticky=W)

        username.grid(row=3, column=0)
        self.username.grid(row=3, column=1)

        password.grid(row=5, column=0)
        self.password.grid(row=5, column=1)
        login_button.grid (row=7, column=1, columnspan=1)

        register_button.grid(row=7, column=0, columnspan=1)

        self._root.grid_columnconfigure(1, weight=1)
        register_button.bind("<Button-1>", self.show_register_page)
        login_button.bind("<Button-1>", self.handle_login)

      
    def start(self):
        """ Initializing function.
        """  
        self.show_login_page()




