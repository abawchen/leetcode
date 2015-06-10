import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.013_roman_to_integer', fromlist='*')


class Test012(unittest.TestCase):

    def test_romanToInt(self):
        s = solutions.Solution()

        self.assertEqual(s.romanToInt("I"), 1)
        self.assertEqual(s.romanToInt("II"), 2)
        self.assertEqual(s.romanToInt("III"), 3)
        self.assertEqual(s.romanToInt("IV"), 4)
        self.assertEqual(s.romanToInt("V"), 5)
        self.assertEqual(s.romanToInt("VI"), 6)
        self.assertEqual(s.romanToInt("VII"), 7)
        self.assertEqual(s.romanToInt("VIII"), 8)
        self.assertEqual(s.romanToInt("IX"), 9 )
        self.assertEqual(s.romanToInt("X"), 10)

        self.assertEqual(s.romanToInt("XXVIII"), 28)
        self.assertEqual(s.romanToInt("XXIX"), 29)

        self.assertEqual(s.romanToInt("XL"), 40)
        self.assertEqual(s.romanToInt("XLI"), 41)


        self.assertEqual(s.romanToInt("LXXXIX"), 89)

        self.assertEqual(s.romanToInt("XCVIII"), 98)
        self.assertEqual(s.romanToInt("XCIX"), 99)

        
        self.assertEqual(s.romanToInt("CCCXVI"), 316)

        self.assertEqual(s.romanToInt("CD"), 400)
        self.assertEqual(s.romanToInt("CDXCIX"), 499)


        self.assertEqual(s.romanToInt("DCCCXCIV"), 894)

        self.assertEqual(s.romanToInt("MCDXCIX"), 1499)

        self.assertEqual(s.romanToInt("MMMCMXCIX"), 3999)



if __name__ == '__main__':
    unittest.main()
