import unittest
from string import ascii_lowercase, digits
from utilities.utilities import generate_id

class TestUtilities(unittest.TestCase):
    def test_generated_id_is_right_length(self):
        test_id = generate_id()
        self.assertEqual(len(test_id), 4)

    def test_generated_id_is_alphanumeric(self):
        test_id = generate_id()
        chars = ascii_lowercase + digits
        for char in test_id:
            self.assertTrue((char in chars))
