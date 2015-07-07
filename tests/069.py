import unittest
import sys
import itertools
sys.path.append('./')

solutions = __import__('solutions.069_sqrt_x', fromlist='*')


class Test(unittest.TestCase):

    def test_mySqrt(self):
        s = solutions.Solution()

        for i in xrange(1, 10000000):
            self.assertEqual(s.mySqrt(i), int(pow(i, 0.5)))


if __name__ == '__main__':
    unittest.main()
