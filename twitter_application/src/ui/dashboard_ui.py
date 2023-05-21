from tkinter import Tk, ttk, W
from tkinter import *
from services.user_service import UserService
from services.tweet_service import TweetService
from services.like_service import LikeService
from services.comment_service import CommentService
from db_connection import get_db_connection
import time
import uuid
import os


def show_dashboard(self):
    """_summary_
    """        
    self.hide_current_view()
    heading = ttk.Label(master=self._root, text="Dashboard",
                        foreground="white",  background="black")
    heading.grid(row=0, column=0, columnspan=2, sticky=W)

    """ img = Image.open(os.path.join(os.path.dirname(__file__), 'twitter_official.png'))
    resized_image= img.resize((200,200), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    pic_label = ttk.Label(image=new_image)
    pic_label.grid(row=0, column=0)  """
    
    self.tweet = ttk.Entry(master=self._root)
    self.tweet.grid(row=1, column=1)

    self.tweet_error_variable = StringVar()

    self.tweet_error_label = ttk.Label(
            master=self._root,
            textvariable=self.tweet_error_variable,
            foreground="red"
        )

    self.tweet_error_label.grid(row =2, column =1)

      
    post_tweet_button = ttk.Button(master=self._root, text="Post tweet")

    post_tweet_button.grid (row=1, column=2)

    post_tweet_button.bind("<Button-1>", self.post_tweet)
    
    self.display_tweets()


def display_tweets(self):
    """_summary_
    """  

    tweets = self.tweet_service.return_tweets()
    for i in range(0,len(tweets)):
        
        message = StringVar()
        message.set(tweets[i][0].message)
        
        user = StringVar()
        user.set(f"@{tweets[i][1]}")

        picture_url = StringVar()
        picture_url.set(tweets[i][0].picture_url)

        likes = StringVar()
        likes.set(f"{tweets[i][2]}")

        user_label = Label(master=self._root, textvariable = user )
        user_label.grid(row=303+i*2, column=0)

        message_label = Label(master=self._root, textvariable = message )
        message_label.grid(row=303+i*2, column=1)

        like_label = Label(master=self._root, textvariable = likes )
        like_label.grid(row=303+i*2, column=2)
 
        likebutton = ttk.Button(master=self._root, text="Like", command= lambda t= f"{tweets[i][0].id}": self.like_button_clicked(t, self.userinstance.id))
        likebutton.grid(row=303+i*2, column=3)

        view_comments = ttk.Button(master=self._root, text="View comments", command= lambda t= f"{tweets[i][0].id}": self.show_comment_view(t, self.userinstance.id))
        view_comments.grid(row=303+i*2, column=4)
   



    
   
    

        



        
           

           
          