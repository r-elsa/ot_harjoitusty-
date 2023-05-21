from tkinter import Tk, ttk, W
from tkinter import *
import uuid

def show_login_page(self, event=None):
        """ Function that renders the login - page

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
        self.login_error_label.grid(row=501, column=1)

        login_button = ttk.Button(master=self._root, text="LOGIN")
        login_button.grid(row=7, column=1, columnspan=1)
        login_button.bind("<Button-1>", self.handle_login)

        register_button = ttk.Button(master=self._root, text="REGISTER")
        register_button.grid(row=7, column=0, columnspan=1)
        register_button.bind("<Button-1>", self.show_register_page)

def handle_login(self, event=None):
        """ function, which handles user login and raises ValueError on invalid input
        """

        try:
            username = self.username.get()
            password = self.password.get()
            if not (username and password):
                raise ValueError('Empty input field')

            successful_login, logged_in_user = self.user_service.login(
                username, password)

            if not successful_login:
                raise ValueError('wrong username or password')

            self.show_dashboard()
            self.display_tweets()
            self.userinstance = logged_in_user

        except ValueError as e:
            self.login_error_variable.set(e)
            self.login_error_label.grid(row=6, column=1)