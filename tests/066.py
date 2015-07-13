import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.066_plus_one', fromlist='*')


class Test(unittest.TestCase):


    def test_plusOne(self):

        s = solutions.Solution()

        for i in xrange(10000):
            digits = [ int(n) for n in str(i) ]
            self.assertEqual(s.plusOne(digits), [ int(n) for n in str(i+1) ])


if __name__ == '__main__':
    unittest.main()
