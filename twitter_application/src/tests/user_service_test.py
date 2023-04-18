
import unittest
from services.user_service import UserService
from services.tweet_service import TweetService
from services.like_service import LikeService
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
        tweet.create_tweet("6f4rd","1",time.time(), "This is a tweet", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Logo_of_Twitter%2C_Inc..svg/1024px-Logo_of_Twitter%2C_Inc..svg.png", "This is a textfield")
        created_tweet = tweet.return_tweets()
        self.assertEqual(created_tweet[0].message, "This is a tweet")
    
    def test_like(self):
        new_like = LikeService()
        new_like.like("g3w4tfw")
        created_like = new_like.return_likes()
        self.assertEqual(created_like[0].tweet_id, "g3w4tfw")


    
    
    

     
