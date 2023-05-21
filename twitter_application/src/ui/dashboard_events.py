import uuid
import time


def post_tweet(self, event):
    
    """ Function for creating new tweet

    Args:
        event (event): user clicked
    
    Raises:
        ValueError: on empty input
    """

    try:
        tweet = self.tweet.get()
        if not tweet:
            raise ValueError('Empty input')

        self.tweet_service.create_tweet(
            str(uuid.uuid4()), self.userinstance.user_id, time.time(), tweet,  "picture_url")
        self.show_dashboard()

    except ValueError as e:
        self.tweet_error_variable.set(e)
        self.tweet_error_label.grid(row=2, column=1)


def like_button_clicked(self, tweet_id, user_id):
    """ Function of calling Userservice to add like to db and to display tweets

    Args:
        tweet_id (string): id of tweet, to which the like belongs
        user_id (string): id of user who liked the tweet
    """    
  
    self.like_service.like(tweet_id, user_id)
    self.display_tweets()


def comment_button_clicked(self, tweet_id, user_id):
    """ Function, which leads user to view comments

    Args:
        tweet_id (string): id of tweet, to which comment belongs
        user_id (string): user id 

    Raises:
        ValueError: on empty input
    """    
    try:
        message = self.comment.get()
        if not message:
            raise ValueError('Empty input')

        self.comment_service.comment(tweet_id, user_id, message)
        self.show_comment_view(tweet_id, user_id)

    except ValueError as e:
        self.comment_error_variable.set(e)
        self.comment_error_label.grid(row=2, column=1)
