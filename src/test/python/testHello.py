# import unittest
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#     def test_more(self):
#         self.assertEqual(1+2, 3)
#
#
# if __name__ == '__main__':
#     unittest.main()

import pytest

# sys.path.append('../src/main/python')

def test_sum1():
    assert 1 + 2 == 3, "Should be 3"

def test_sum2():
    assert 1 + 2 == 3, "Should be 3"
