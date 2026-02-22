import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
     """Tests for 'name function.py"""
     def test_first_last_name(self):
         """Do names like 'Marcelo Salvador' work"""
         formatted_name = get_formatted_name('Marcelo','Salvador')
         self.assertEqual(formatted_name, 'Marcelo Salvador')

     def test_first_last_middle_name(self):
         """Do names like 'Wolfgang Amadeus Mozar' work?"""
         formatted_name = get_formatted_name(
             'wolfgang','mozart','amadeus'
         )
         self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == "__main__":
    unittest.main()