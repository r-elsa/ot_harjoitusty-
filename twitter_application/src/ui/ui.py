from tkinter import Tk, ttk, W
from tkinter import *
from services.user_service import UserService
from services.tweet_service import TweetService
from services.like_service import LikeService
from services.comment_service import CommentService
from db_connection import get_db_connection



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
        self.userinstance = None
        self.tweet_service = TweetService(get_db_connection())
        self.user_service = UserService(get_db_connection())
        self.like_service = LikeService(get_db_connection())
        self.comment_service = CommentService(get_db_connection())

    from .dashboard_view import show_dashboard, display_tweets
    from .register_view import handle_register, show_register_page
    from .comment_view import show_comment_view, display_comments
    from .dashboard_events import comment_button_clicked,  like_button_clicked,  post_tweet
    from .login_view import show_login_page, handle_login

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

   
    def start(self):
        """ Initializing function.
        """
        self.show_login_page()

