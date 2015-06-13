import unittest
import sys
sys.path.append('./')
solutions = __import__('solutions.008_string_to_integer', fromlist='*')


class Test022(unittest.TestCase):

    def test_myAtoi(self):
        s = solutions.Solution()

        self.assertEqual(s.myAtoi("0"), 0)
        self.assertEqual(s.myAtoi("10"), 10)
        self.assertEqual(s.myAtoi("1012341"), 1012341)
        self.assertEqual(s.myAtoi("    1012341"), 1012341)
        self.assertEqual(s.myAtoi("    +1012341"), 1012341)
        self.assertEqual(s.myAtoi("    -1012341"), -1012341)

        self.assertEqual(s.myAtoi("    +1012341a"), 1012341)
        self.assertEqual(s.myAtoi("    -1012341b"), -1012341)


        self.assertEqual(s.myAtoi("    -abcdd"), 0)
        self.assertEqual(s.myAtoi("    abcdd"), 0)

        self.assertEqual(s.myAtoi("    "), 0)
        self.assertEqual(s.myAtoi(""), 0)

        self.assertEqual(s.myAtoi("a100"), 0)
        self.assertEqual(s.myAtoi("-a100"), 0)


        self.assertEqual(s.myAtoi("+-2"), 0)

        self.assertEqual(s.myAtoi("+2"), 2)
        self.assertEqual(s.myAtoi("+2+"), 2)

        self.assertEqual(s.myAtoi("  -0012a42"), -12)

        self.assertEqual(s.myAtoi("  -0012 a42"), -12)

        self.assertEqual(s.myAtoi(""), 0)

        self.assertEqual(s.myAtoi(" - 321"), 0)

        self.assertEqual(s.myAtoi(" -321 afe"), -321)
                    
        


if __name__ == '__main__':
    unittest.main()
