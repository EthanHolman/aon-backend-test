import unittest
from services import calcWeekTotals

class TestStringMethods(unittest.TestCase):
    def test_week_lengths_accurate(self):
        pass

    def test_no_dates(self):
        dates = []
        calcWeekTotals(2021, 12, dates)

    def test_date_first_week(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_date_last_week(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()