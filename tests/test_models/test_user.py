#!/usr/bin/python3
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up the User instance for testing"""
        self.user = User()

    def tearDown(self):
        """Clean up after each test"""
        del self.user

    def test_inherit(self):
        """Test if User inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attr(self):
        """Test the attributes of User"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test__arguments(self):
        """Test  User with arguments"""
        user = User(email="agwelidancan32@gmail.com", password="123", first_name="Dan", last_name="tumbo")
        self.assertEqual(user.email, "agwelidancan32@gmail.com")
        self.assertEqual(user.password, "123")
        self.assertEqual(user.first_name, "Dan")
        self.assertEqual(user.last_name, "tumbo")

    def test_initialization_with_kwargs(self):
        """Test initializing User
        keyword arguments"""
        kwargs = {"email": "agwelidancan321@gmail.com", "password": "223", "first_name": "dory", "last_name": "Nyaundi"}
        user = User(**kwargs)
        self.assertEqual(user.email, "agwelidancan321@gmail.com")
        self.assertEqual(user.password, "223")
        self.assertEqual(user.first_name, "dory")
        self.assertEqual(user.last_name, "Nyaundi")

if __name__ == "__main__":
    unittest.main()

