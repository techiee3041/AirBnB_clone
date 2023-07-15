#!/usr/bin/python3
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Make up Amenity instance for testing"""
        self.amenity = Amenity()

    def doors(self):
        """Clean the test"""
        del self.amenity

    def test_inherits(self):
        """Test if Amenity inherits from BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attr(self):
        """Test of attributes of Amenity"""
        self.assertEqual(self.amenity.name, "")

    def test_arguments(self):
        """Test initializing Amenity"""
        amenity = Amenity(name="garden")
        self.assertEqual(amenity.name, "garden")

    def test_kwargs(self):
        """Test initializing Amenity with keyword arguments"""
        kwargs = {"name": "dining"}
        amenity = Amenity(**kwargs)
        self.assertEqual(amenity.name, "dining")

if __name__ == "__main__":
    unittest.main()

