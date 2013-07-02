import unittest
""" Unit tests for technical indicators...
"""

class aroon_test(unittest.TestCase):
    """structure the tests with the function name and _test"""
    def test(self):
        self.assertEqual(aroon(1), 1)


if __name__ == '__main__':
    unittest.main()