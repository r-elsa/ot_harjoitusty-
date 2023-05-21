from entities.tweet import Tweet
from db_connection import get_db_connection


def get_tweet_by_row(row):
    return (Tweet(row[0], row[1], row[2], row[3], row[4]), row[5], row[6]) if row else None


class TweetService:
    """ Class, which creates and returns tweets 
        as well as returns tweet message (for commentservice)
    """

    def __init__(self, connection):
        self.connection = connection

    def create_tweet(self, tweet_id, user_id, send_time, message, picture_url):
        """ Create/Post a new tweet

        Args:
            tweet_id (string)): id of tweet 
            user (string): id of user who posted tweet
            send_time (date): date when tweet was posted
            message (string): content of tweet
            picture_url (string): url of picture added to tweet
        """

        new_tweet = Tweet(tweet_id, user_id, send_time, message, picture_url)

        cursor = self.connection.cursor()
        cursor.execute(
            "insert into tweet (tweet_id, user_id, send_time,"\
            "message, picture_url) values (?, ?, ?, ?, ?)",
            (new_tweet.tweet_id, new_tweet.user_id, new_tweet.send_time,
             new_tweet.message, new_tweet.picture_url,)
        )
        self.connection.commit()

    def get_tweet_message(self, tweet_id):
        """ function that returns twet message based on tweet id

        Args:
            tweet_id (string)): id of tweet 
        """

        cursor = self.connection.cursor()

        cursor.execute(
            "select message from tweet where tweet_id = ?",
            (tweet_id,)
        )
        row = cursor.fetchone()[0]
        return row

    def return_tweets(self):
        """ Returns all tweets, orders by time and limits to 30 tweets

        Returns:
            array: Array of tweet - objects.
        """
        cursor = self.connection.cursor()
        cursor.execute("select tweet.tweet_id,tweet.user_id, tweet.send_time,"\
                      "tweet.message, tweet.picture_url, user.username,"\
                      "COUNT(like.tweet_id) from tweet LEFT JOIN user ON" \
                      " tweet.user_id = user.user_id LEFT JOIN like"\
                      " ON tweet.tweet_id = like.tweet_id GROUP BY tweet.tweet_id,"\
                      " like.tweet_id ORDER BY tweet.send_time DESC LIMIT 30")

        rows = cursor.fetchall()
        return list(map(get_tweet_by_row, rows))

tweet_service = TweetService(get_db_connection())
