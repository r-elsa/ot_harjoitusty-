import uuid
from entities.tweet import Tweet

class TweetService:
    def __init__(self):
        self.id = uuid.uuid4
        self.tweets = []

    def create_tweet(self, id, user, send_time, message, picture_url):
        self.tweets.append(Tweet(id, user, send_time, message, picture_url ))

    def return_tweets(self):
        return self.tweets

