import unittest
from operator import truediv
import sys
sys.path.append('./')

solutions = __import__('solutions.029_divide_two_integers', fromlist='*')


class Test029(unittest.TestCase):

    def test_divide(self):
        s = solutions.Solution()

        dividend, divisor = 49, 7
        self.assertEqual(s.divide(dividend, divisor), self._divide(dividend, divisor))

        dividend, divisor = 55, 7
        self.assertEqual(s.divide(dividend, divisor), self._divide(dividend, divisor))

        dividend, divisor = 56, 7
        self.assertEqual(s.divide(dividend, divisor), self._divide(dividend, divisor))

        dividend, divisor = 56+29, 7
        self.assertEqual(s.divide(dividend, divisor), self._divide(dividend, divisor))

        dividend, divisor = -1020450018, 2091335377
        self.assertEqual(s.divide(dividend, divisor), self._divide(dividend, divisor))

        dividend, divisor = -2147483648, -1
        self.assertEqual(s.divide(dividend, divisor), 2147483647)

        dividend, divisor = -999511578, -2147483648
        self.assertEqual(s.divide(dividend, divisor), self._divide(dividend, divisor))

        dividend, divisor = -2147483648, 1
        self.assertEqual(s.divide(dividend, divisor), self._divide(dividend, divisor))

    def _divide(self, dividend, divisor):
        return int(truediv(dividend, divisor))


        
if __name__ == '__main__':
    unittest.main()
