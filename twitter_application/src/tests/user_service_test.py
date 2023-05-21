
import unittest
from services.user_service import UserService
from services.tweet_service import TweetService
from services.like_service import LikeService
from services.comment_service import CommentService
import time


class TestUserService(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_user_registered(self):
        user = UserService()
        user.create_user("testname", "testusername", "testpwd123p2")
        amount_of_users = user.count_users()
        self.assertEqual(amount_of_users, 1)

    def test_create_tweet(self):
        tweet = TweetService()
        tweet.create_tweet("d2c38bbb-0fce-496d-bec7-d60348ed69fe", "user1", time.time(), "This is a tweet",
                           "img")
        created_tweet = tweet.return_tweets()
        self.assertEqual(created_tweet[0].message, "This is a tweet")

    def test_like(self):
        new_like = LikeService()
        new_like.like("d2c38bbb-0fce-496d-bec7-d60348ed69fe")
        created_like = new_like.return_likes()
        self.assertEqual(created_like[0].tweet_id,
                         "d2c38bbb-0fce-496d-bec7-d60348ed69fe")

    def test_comment(self):
        new_comment = CommentService()
        new_comment.comment("d2c38bbb-0fce-496d-bec7-d60348ed69fe")
        created_comment = new_comment.return_comments()
        self.assertEqual(
            created_comment[0].tweet_id, "d2c38bbb-0fce-496d-bec7-d60348ed69fe")
