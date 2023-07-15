#!/usr/bin/python3
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        """ instance for testing"""
        self.place = Place()

    def tear_Down(self):
        """Clean up after each test"""
        del self.place

    def test_inherit(self):
        """Test if Place inherits from BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Test the attributes of Place"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_initials(self):
        """Test initializing Place with arguments"""
        place = Place(
            city_id="1234",
            user_id="234",
            name="tumbo",
            description="A place to be",
            number_rooms=3,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=1000,
            latitude=51.5065,
            longitude=-0.1248,
            amenity_ids=[1, 2, 3]
        )
        self.assertEqual(place.city_id, "1234")
        self.assertEqual(place.user_id, "234")
        self.assertEqual(place.name, "tumbo")
        self.assertEqual(place.description, "A place to be")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 1000)
        self.assertEqual(place.latitude, 51.5065)
        self.assertEqual(place.longitude, -0.1248)
        self.assertEqual(place.amenity_ids, [1, 2, 3])

    def test_initialization_with_kwargs(self):
        """Test initializing Place with keyword arguments"""
        kwargs = {
            "city_id": "123",
            "user_id": "011",
            "name": "jacked",
            "description": "An exquisite villa with stunning ocean views",
            "number_rooms": 4,
            "number_bathrooms": 3,
            "max_guest": 8,
            "price_by_night": 5000,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "amenity_ids": [4, 5, 6]
        }
        place = Place(**kwargs)
        self.assertEqual(place.city_id, "789")
        self.assertEqual(place.user_id, "012")
        self.assertEqual(place.name, "Luxury Villa")
        self.assertEqual(place.description, "An exquisite villa with stunning ocean views")
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.number_bathrooms, 3)
        self.assertEqual(place.max_guest, 8)
        self.assertEqual(place.price_by_night, 500)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, [4, 5, 6])

if __name__ == "__main__":
    unittest.main()

