import uuid
import time
from entities.like import Like
from db_connection import get_db_connection


def get_like_by_row(row):
    return Like(row[0], row[1], row[2], row[3]) if row else None


class LikeService:
    """ Class, which adds and returns likes and also checks if a user has already liked a tweet.
    """

    def __init__(self, connection):
        """ The contructor of the class LikeService

        Args:
            connection : connection to database
        """
        self.connection = connection

    def like(self, tweet_id, user_id):
        """ Add a like

        Args:
            tweet_id (string): Id of the tweet that is being liked.
            user_id (string): Id of user who likes the tweet
        """
        already_liked = self.like_exists(user_id, tweet_id)

        if already_liked:
            return False

        new_like = Like(str(uuid.uuid4()), user_id, tweet_id, time.time())
        cursor = self.connection.cursor()
        cursor.execute(
            "insert into like (like_id, user_id, tweet_id, send_time) values (?, ?, ?, ?)",
            (new_like.id, new_like.user_id,
                new_like.tweet_id, new_like.send_time)
        )
        self.connection.commit()
        return True

    def like_exists(self, user_id, tweet_id):
        """ check if like already exists

        Args:
            tweet_id (string): Id of the tweet that is being liked.
            user_id (string): Id of user who likes the tweet
        """

        cursor = self.connection.cursor()
        cursor.execute(
            "select * from like where user_id = ? and tweet_id = ?",
            (user_id, tweet_id)
        )

        row = cursor.fetchone()
        if row is not None:
            return True
        return False

    def return_likes(self):
        """ Return all likes.

        Returns:
            array: Array of like - objects.
        """
        cursor = self.connection.cursor()
        cursor.execute("select * from like")
        rows = cursor.fetchall()
        return list(map(get_like_by_row, rows))


like_service = LikeService(get_db_connection())
