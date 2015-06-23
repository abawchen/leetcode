import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.224_basic_calculator', fromlist='*')


class Test(unittest.TestCase):

    def test_calculate(self):
        s = solutions.Solution()

        st = "1 + 1"
        self.assertEqual(s.calculate(st), eval(st))

        st = " 2-1 "
        self.assertEqual(s.calculate(st), eval(st))

        st = " 2-1 + 2 "
        self.assertEqual(s.calculate(st), eval(st))

        st = " 2-(1 + 200000) "
        self.assertEqual(s.calculate(st), eval(st))

        st = "(1+2)"
        self.assertEqual(s.calculate(st), eval(st))

        st = "(1+(400+5+2)-3)+(6+8)"
        self.assertEqual(s.calculate(st), eval(st))


        st = "(19+29)-(25+13)"
        self.assertEqual(s.calculate(st), eval(st))

        st = "(333) + (900-10000) + 3"
        self.assertEqual(s.calculate(st), eval(st))


if __name__ == '__main__':
    unittest.main()

