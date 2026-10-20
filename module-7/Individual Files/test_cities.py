"""
Author: Nicholas Zankl
Date: September 20, 2026
Course: CSD-325
Assignment: Module 7.2 - Test Cases (test_cities.py)
Description: Unit tests to verify string output formatting for the city_country function.
"""

import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does a simple city and country pair work?"""
        formatted_city = city_country('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does passing population work?"""
        formatted_city = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - population 5000000')

    def test_city_country_population_language(self):
        """Does passing both population and language work?"""
        formatted_city = city_country('santiago', 'chile', population=5000000, language='spanish')
        self.assertEqual(formatted_city, 'Santiago, Chile - population 5000000, Spanish')

if __name__ == '__main__':
    unittest.main()
