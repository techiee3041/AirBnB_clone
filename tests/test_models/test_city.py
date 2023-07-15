#!/usr/bin/python3
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        """Make the City instance for testing"""
        self.city = City()

    def cities(self):
        """make tide each test"""
        del self.city

    def test_inherits(self):
        """Test if City inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test the attributes of City"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_initialization_with_arguments(self):
        """Test initializing with arguments"""
        city = City(state_id="ke", name="kenya")
        self.assertEqual(city.state_id, "ke")
        self.assertEqual(city.name, "kenya")

    def test_kwargs(self):
        """Test initializing City with keyword arguments"""
        kwargs = {"state_id": "N", "name": "Nairobi"}
        city = City(**kwargs)
        self.assertEqual(city.state_id, "N")
        self.assertEqual(city.name, "Nairobi")

if __name__ == "__main__":
    unittest.main()

