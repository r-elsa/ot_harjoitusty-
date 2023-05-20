from tkinter import Tk, ttk, W
from tkinter import *
from PIL import ImageTk, Image  
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
    print(self.userinstance)
    self.tweet_service.create_tweet(str(uuid.uuid4()),self.userinstance.id, time.time(), tweet,  "picture_url") 



    self.display_tweets()

    
def display_tweets(self):
    """_summary_
    """        
    tweets = self.tweet_service.return_tweets()

    img = Image.open(os.path.join(os.path.dirname(__file__), 'twitter_official.png'))
    resized_image= img.resize((50,50), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    pic_label = ttk.Label(image=new_image)
    pic_label.grid(row=3, column=1) 
 


    for i in range(0,len(tweets)):
        message = StringVar()
        message.set(tweets[i][0].message)
        user = StringVar()
        user.set(f"@{tweets[i][1]}")

        picture_url = StringVar()
        picture_url.set(tweets[i][0].picture_url)

        user_label = Label(master=self._root, textvariable = user )
        user_label.grid(row=303+i*2, column=0)
      
      
        message_label = Label(master=self._root, textvariable = message )
        message_label.grid(row=303+i*2, column=2)
        likebutton = ttk.Button(master=self._root, text="Like", command= lambda t= f"{tweets[i][0].id}": self.like_service.like(t, tweets[i][0].user_id))
        likebutton.grid(row=303+i*2, column=3)

        view_comments = ttk.Button(master=self._root, text="View comments", command= lambda t= f"{tweets[i][0].id}": self.comment_service.comment(t,tweets[i][0].user_id))
        view_comments.grid(row=303+i*2, column=4)


        
           

           
          