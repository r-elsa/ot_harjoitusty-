# Instructions 

1. Download newest release

2. Add configurations

- modify database (DATABASE_FILENAME) in  *.env*- file to your liking. 

3. Install dependencies

```bash
poetry install
```

4. Start application 

```bash
poetry run invoke start
```

Following, a *Tkinter* window should open with possibilities to login or register. 

A pre existing user can login to the application. With the *username* ``` chelseayu ``` and *password* ``` chelseayu_8746 ``` one can login.

![](./images/login_view.jpg)


A new user can register from the register - view. The user is notified if the username already exists.

![](.//images/reqister_view.jpg)

The wall/dashboard shows all tweets. The user can like and write their own tweet. 
![](./images/dashboard_view.jpg)

The user can comment on tweets and then navigate back to the wall of tweets.

![](./images/comment_view.jpg)
