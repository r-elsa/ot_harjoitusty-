from tkinter import Tk, ttk, W
from services.user_service import UserService


class UI:
    def __init__(self, root):
        self._root = root

    def handle_button_click(self, event):
        name = self.name.get()
        username = self.username.get()
        password = self.password.get()

        instance = UserService()
        instance.create_user(name, username, password)
        instance.return_users()

        # check if user exists (username already exists)

        # if username not exists --> create user

    def return_users(self):
        for i in self.users:
            print(i)

    def start(self):
        heading = ttk.Label(master=self._root, text="Register",
                            foreground="white",  background="black")

        name = ttk.Label(master=self._root, text="Name")
        self.name = ttk.Entry(master=self._root)

        username = ttk.Label(master=self._root, text="Username")
        self.username = ttk.Entry(master=self._root)

        password = ttk.Label(master=self._root, text="Password")
        self.password = ttk.Entry(master=self._root)

        button = ttk.Button(master=self._root, text="REGISTER")

        heading.grid(row=0, column=0, columnspan=2, sticky=W)

        name.grid(row=1, column=0)
        self.name.grid(row=1, column=1)

        username.grid(row=3, column=0)
        self.username.grid(row=3, column=1)

        password.grid(row=5, column=0)
        self.password.grid(row=5, column=1)

        button.grid(row=7, column=0, columnspan=2)

        self._root.grid_columnconfigure(1, weight=1)
        button.bind("<Button-1>", self.handle_button_click)
