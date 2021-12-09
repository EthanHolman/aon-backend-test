import unittest
from services.fib import findNFibs


class TestFibService(unittest.TestCase):
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
