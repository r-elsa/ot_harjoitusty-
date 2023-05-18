from tkinter import Tk, ttk, W
from tkinter import *
from services.user_service import UserService
from services.tweet_service import TweetService
from services.like_service import LikeService
from services.comment_service import CommentService
from db_connection import get_db_connection
import time
import uuid

        
        


def show_dashboard(self):
    """_summary_
    """        
    self.hide_current_view()
    heading = ttk.Label(master=self._root, text="Dashboard",
                        foreground="white",  background="black")
    
    self.tweet = ttk.Entry(master=self._root)
    
    post_tweet_button = ttk.Button(master=self._root, text="Post tweet")
    self.tweet.grid(row=1, column=1)
    heading.grid(row=0, column=0, columnspan=2, sticky=W)
    post_tweet_button.grid (row=1, column=2, columnspan=1)

    self._root.grid_columnconfigure(1, weight=1)
    post_tweet_button.bind("<Button-1>", self.post_tweet)
    self.tweet_service.return_tweets()


def post_tweet(self,event):
    """_summary_

    Args:
        event (_type_): _description_
    """        
    tweet = self.tweet.get()
    self.tweet_service.create_tweet(str(uuid.uuid4()),str(uuid.uuid4()), time.time(), tweet,  "picture_url") 



    self.display_tweets()

    
def display_tweets(self):
    """_summary_
    """        
    tweets = self.tweet_service.return_tweets()
      
    for i in range(0,len(tweets)):
        message = StringVar()
        message.set(tweets[i].message)
        user = StringVar()
        user.set(tweets[i].user_id)
        picture_url = StringVar()
        picture_url.set(tweets[i].picture_url)
    
        user_label = Label(master=self._root, textvariable = user )
        user_label.grid(row=3+i*2, column=2)

        picture_url_label = Label(master=self._root, textvariable = picture_url )
        picture_url_label.grid(row=3+i*2, column=2)

        message_label = Label(master=self._root, textvariable = message )
        message_label.grid(row=3+i*2, column=2)
        likebutton = ttk.Button(master=self._root, text="Like", command= lambda t= f"{tweets[i].id}": self.like_service.like(t))
        likebutton.grid(row=3+i*2, column=2)

        view_comments = ttk.Button(master=self._root, text="View comments", command= lambda t= f"{tweets[i].id}": self.comment_service.comment(t))
        view_comments.grid(row=3+i*2, column=2)