#!/usr/bin/python3
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up the Review instance for testing"""
        self.review = Review()

    def tearDown(self):
        """Clean up after each test"""
        del self.review

    def test_inheritance(self):
        """Test if Review inherits from BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Test the attributes of Review"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_iniarguments(self):
        """Test initializing Review with arguments"""
        review = Review(place_id="123", user_id="456", text="Great place!")
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great place!")

    def test_kwargs(self):
        """Test initializing Review with keyword arguments"""
        kwargs = {"place_id": "123", "user_id": "1234", "text": "Amazing experience!"}
        review = Review(**kwargs)
        self.assertEqual(review.place_id, "789")
        self.assertEqual(review.user_id, "012")
        self.assertEqual(review.text, "Amazing experience!")

if __name__ == "__main__":
    unittest.main()

