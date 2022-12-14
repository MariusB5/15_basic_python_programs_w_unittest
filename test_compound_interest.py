import unittest
from compound_interest import compound_interest


p = 2500
r = 3.5
t = 5


class TestCompoundInterest(unittest.TestCase):
    def test_compound_interest(self):
        self.assertEqual(compound_interest(p, r, t), 2969.22)


if __name__ == '__main__':
    unittest.main()
