import unittest
from simple_interest import simple_interest


# variables
p = 2500
r = 3.5
t = 5


# unittest documentation at 
# # https://docs.python.org/3/library/unittest.html#module-unittest
class TestSimpleInterest(unittest.TestCase):
    def test_simple_interest(self):
        self.assertEqual(simple_interest(p, r, t), 437.5)


if __name__ == '__main__':
    unittest.main()
