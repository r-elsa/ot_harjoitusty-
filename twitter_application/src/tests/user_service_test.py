
import unittest
from services.user_service import UserService


class TestUserService(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def user_registered(self):
        user = UserService()
        user.create_user(self, "testname", "testusername", "testpwd123p2")
        amount_of_users = amount_of_users()
        self.assertEqual(amount_of_users, 1)
