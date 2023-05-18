from tkinter import Tk, ttk, W
from tkinter import *
import uuid

def handle_register(self, event=None):
        """_summary_

        Args:
            event (_type_, optional): _description_. Defaults to None.
        """         
        name = self.name.get()
        username = self.username.get()
        password = self.password.get()

        self.user_service.create_user(str(uuid.uuid4),name, username, password, "url", False)
        self.user_service.return_users()

        self.username= username
        self.show_dashboard()

def show_register_page(self, event = None):
        """_summary_

        Args:
            event (_type_, optional): _description_. Defaults to None.
        """        
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
    

     