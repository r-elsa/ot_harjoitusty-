
import unittest
from services.user_service import UserService


class TestUserService(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_user_registered(self):
        user = UserService()
        user.create_user("testname", "testusername", "testpwd123p2")
        amount_of_users = user.count_users()
        self.assertEqual(amount_of_users, 1)

     
