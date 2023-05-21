import uuid
import time


def post_tweet(self, event):
    """_summary_

    Args:
        event (_type_): _description_
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
    """_summary_
    """
    self.like_service.like(tweet_id, user_id)
    self.display_tweets()


def comment_button_clicked(self, tweet_id, user_id):
    try:
        message = self.comment.get()
        if not message:
            raise ValueError('Empty input')

        self.comment_service.comment(tweet_id, user_id, message)
        self.show_comment_view(tweet_id, user_id)

    except ValueError as e:
        self.comment_error_variable.set(e)
        self.comment_error_label.grid(row=2, column=1)
