import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Tests for the Amenity  class"""

    def setUp(self):
        """Test that class can be instatiated"""
                self.a1 = Amenity()

    def test_is_instance(self):
        """Test that an instance is of type Amenity"""
        self.assertIsInstance(self.a1, Amenity)
