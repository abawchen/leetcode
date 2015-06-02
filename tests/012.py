import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.012_integer_to_roman', fromlist='*')


class Test012(unittest.TestCase):

    def test_intToRoman(self):
        s = solutions.Solution()

        self.assertEqual(s.intToRoman(1), "I")
        self.assertEqual(s.intToRoman(2), "II")
        self.assertEqual(s.intToRoman(3), "III")
        self.assertEqual(s.intToRoman(4), "IV")
        self.assertEqual(s.intToRoman(5), "V")
        self.assertEqual(s.intToRoman(6), "VI")
        self.assertEqual(s.intToRoman(7), "VII")
        self.assertEqual(s.intToRoman(8), "VIII")
        self.assertEqual(s.intToRoman(9), "IX")
        self.assertEqual(s.intToRoman(10), "X")

        self.assertEqual(s.intToRoman(28), "XXVIII")
        self.assertEqual(s.intToRoman(29), "XXIX")

        self.assertEqual(s.intToRoman(40), "XL")
        self.assertEqual(s.intToRoman(41), "XLI")


        self.assertEqual(s.intToRoman(89), "LXXXIX")

        self.assertEqual(s.intToRoman(98), "XCVIII")
        self.assertEqual(s.intToRoman(99), "XCIX")

        
        self.assertEqual(s.intToRoman(316), "CCCXVI")

        self.assertEqual(s.intToRoman(400), "CD")
        self.assertEqual(s.intToRoman(499), "CDXCIX")


        self.assertEqual(s.intToRoman(894), "DCCCXCIV")

        self.assertEqual(s.intToRoman(1499), "MCDXCIX")

        self.assertEqual(s.intToRoman(3999), "MMMCMXCIX")


        for i in xrange(1, 4000):
            s.intToRoman(i)



if __name__ == '__main__':
    unittest.main()
