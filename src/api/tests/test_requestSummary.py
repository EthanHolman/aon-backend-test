import unittest
from datetime import datetime
from services.requestSummary import calcWeekTotals


class TestRequestSummaryService(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()