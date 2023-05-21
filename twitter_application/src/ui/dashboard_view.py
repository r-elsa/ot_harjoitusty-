import time
import uuid
import os
from datetime import datetime
from tkinter import Tk, ttk, W
from tkinter import *
from services.user_service import UserService
from services.tweet_service import TweetService
from services.like_service import LikeService
from services.comment_service import CommentService
from db_connection import get_db_connection


def show_dashboard(self):
    """_summary_
    """
    self.hide_current_view()
    heading = ttk.Label(master=self._root, text="Dashboard",
                        foreground="white",  background="black")
    heading.grid(row=0, column=0, columnspan=2, sticky=W)


    self.tweet = ttk.Entry(master=self._root)
    self.tweet.grid(row=1, column=1)

    self.tweet_error_variable = StringVar()

    self.tweet_error_label = ttk.Label(
        master=self._root,
        textvariable=self.tweet_error_variable,
        foreground="red"
    )

    self.tweet_error_label.grid(row=2, column=1)

    post_tweet_button = ttk.Button(master=self._root, text="Post tweet")

    post_tweet_button.grid(row=1, column=2)

    post_tweet_button.bind("<Button-1>", self.post_tweet)

    self.display_tweets()


def display_tweets(self):
    """_summary_
    """
    tweets = self.tweet_service.return_tweets()
    if not tweets:
            notweets_message =  StringVar()
            notweets_message.set("No tweets yet.")
            notweets_message_label = Label(master=self._root, textvariable=notweets_message)
            notweets_message_label.grid(row=5, column=1)

    for i in range(0, len(tweets)):

        message = StringVar()
        message.set(tweets[i][0].message)

        user = StringVar()
        user.set(f"@{tweets[i][1]}")

        time_of_tweet = StringVar()
        time_of_tweet.set(datetime.fromtimestamp(tweets[i][0].send_time))
            
        likes = StringVar()
        likes.set(f"{tweets[i][2]}")

        user_label = Label(master=self._root, textvariable=user)
        user_label.grid(row=303+i*2, column=0)

        time_of_tweet_label = Label(master=self._root, textvariable=time_of_tweet)
        time_of_tweet_label.grid(row=303+i*2, column=1)

        message_label = Label(master=self._root, textvariable=message)
        message_label.grid(row=303+i*2, column=2)

        like_label = Label(master=self._root, textvariable=likes)
        like_label.grid(row=303+i*2, column=3)

        likebutton = ttk.Button(master=self._root, text="Like",
                                command=lambda t=f"{tweets[i][0].tweet_id}": self.like_button_clicked(t, self.userinstance.user_id))
        likebutton.grid(row=303+i*2, column=4)

        view_comments = ttk.Button(master=self._root, text="View comments",
                                command=lambda t=f"{tweets[i][0].tweet_id}": self.show_comment_view(t, self.userinstance.user_id))
        view_comments.grid(row=303+i*2, column=5)


