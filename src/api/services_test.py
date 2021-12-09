import unittest
from datetime import datetime
from services import calcWeekTotals, findNFibs


class TestStringMethods(unittest.TestCase):
    def test_no_dates(self):
        dates = []
        result = calcWeekTotals(2021, 12, dates)
        expectedResult = [0, 0, 0, 0, 0]
        self.assertListEqual(result, expectedResult)

    def test_dates_outside_month(self):
        dates = [
            datetime(2021, 12, 1),
            datetime(2021, 12, 29),
            datetime(2020, 11, 1),
        ]
        result = calcWeekTotals(2021, 11, dates)
        expectedResult = [0, 0, 0, 0, 0]
        self.assertListEqual(result, expectedResult)

    def test_dates_all_in_month(self):
        dates = [
            datetime(2021, 11, 15),
            datetime(2021, 11, 1),
            datetime(2021, 11, 16)
        ]
        result = calcWeekTotals(2021, 11, dates)
        expectedResult = [1, 0, 2, 0, 0]
        self.assertListEqual(result, expectedResult)

    def test_dates_some_in_month(self):
        dates = [
            datetime(2021, 11, 15),
            datetime(2021, 11, 1),
            datetime(2021, 11, 16),
            datetime(2021, 12, 1),
            datetime(2020, 11, 1)
        ]
        result = calcWeekTotals(2021, 11, dates)
        expectedResult = [1, 0, 2, 0, 0]
        self.assertListEqual(result, expectedResult)

    def test_finding_fibs(self):
        inputValues = [
            0,
            -1,
            6,
            20
        ]
        expectedValues = [
            [],
            [],
            [0, 1, 1, 2, 3, 5],
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
                144, 233, 377, 610, 987, 1597, 2584, 4181]
        ]
        for index, inputVal in enumerate(inputValues):
            result = findNFibs(inputVal)
            self.assertEqual(result, expectedValues[index])

# s = 'hello world'
# self.assertEqual(s.split(), ['hello', 'world'])
# # check that s.split fails when the separator is not a string
# with self.assertRaises(TypeError):
#     s.split(2)


if __name__ == '__main__':
    unittest.main()
