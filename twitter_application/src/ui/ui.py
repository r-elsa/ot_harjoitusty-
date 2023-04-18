from tkinter import Tk, ttk, W
from tkinter import *
from services.user_service import UserService
from services.tweet_service import TweetService
from services.like_service import LikeService
import time
import uuid

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self.username = None
        self.tweet_service= TweetService()
        self.user_service =  UserService()
        self.like_service = LikeService()
    

    def hide_current_view(self):
        list = self._root.grid_slaves()
        for l in list:
            l.destroy()

    def handle_register(self, event=None):   
        name = self.name.get()
        username = self.username.get()
        password = self.password.get()

        self.user_service.create_user(name, username, password)
        self.user_service.return_users()

        self.username= username
        self.show_dashboard()

    
    def handle_login(self, event=None):
        username = self.username.get()
        password = self.password.get()

        instance = UserService()
        instance.login(username, password)
        self.username= username
        self.show_dashboard()
    
    
    def show_login_page(self, event=None):
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
    


    def show_register_page(self, event = None):
        self.hide_current_view()
        heading = ttk.Label(master=self._root, text="Register",
                            foreground="white",  background="black")

        name = ttk.Label(master=self._root, text="Name")
        self.name = ttk.Entry(master=self._root)

        username = ttk.Label(master=self._root, text="Username")
        self.username = ttk.Entry(master=self._root)

        password = ttk.Label(master=self._root, text="Password")
        self.password = ttk.Entry(master=self._root)

        register_button = ttk.Button(master=self._root, text="REGISTER")

        login_button = ttk.Button(master=self._root, text="LOGIN")

        heading.grid(row=0, column=0, columnspan=2, sticky=W)

        name.grid(row=1, column=0)
        self.name.grid(row=1, column=1)

        username.grid(row=3, column=0)
        self.username.grid(row=3, column=1)

        password.grid(row=5, column=0)
        self.password.grid(row=5, column=1)

        login_button.grid (row=7, column=0, columnspan=1)
        
        register_button.grid(row=7, column=1, columnspan=1)

        self._root.grid_columnconfigure(1, weight=1)
        login_button.bind("<Button-1>", self.show_login_page)
        register_button.bind("<Button-1>", self.handle_register)
    

    def show_dashboard(self):
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
        tweet = self.tweet.get()
        self.tweet_service.create_tweet(uuid.uuid4(), self.username, time.time(), tweet,  "picture_url", "picture textfield text") 
        self.display_tweets()
    
       
    def display_tweets(self):
        tweets = self.tweet_service.return_tweets()
      
        for i in range(0,len(tweets)):
            var = StringVar()
            var.set(tweets[i].message)
            label = Label(master=self._root, textvariable = var )
            label.grid(row=3+i*2, column=0)
            likebutton = ttk.Button(master=self._root, text="Like", command= lambda t= f"{tweets[i].id}": self.like_service.like(t))
            likebutton.grid(row=3+i*2, column=1)
    
    def start(self):
        self.show_login_page()
        self.display_tweets()



