import unittest
import utilities

class TestUtilities(unittest.TestCase):
    def test_check_year_valid_ce(self):
        year = utilities.check_year("2021")
        self.assertTrue(year)
    
    def test_check_year_valid_bce(self):
        year = utilities.check_year("299 eaa.")
        self.assertTrue(year)

    def test_check_year_invalid_alpha(self):
        year = utilities.check_year("uhfijdo")
        self.assertFalse(year)

    def test_check_year_invalid_negative(self):
        year = utilities.check_year("-200")
        self.assertFalse(year)

    def test_check_year_invalid_bce(self):
        year = utilities.check_year("udjkdj bce")
        self.assertFalse(year)

