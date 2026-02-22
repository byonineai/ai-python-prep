import unittest

from city_functions import city_country_injective

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        result = city_country_injective("Rio de Janeiro", "Brazil")
        self.assertEqual(result, "14:Rio de Janeiro|6:Brazil")

if __name__ == "__main__":
    unittest.main()