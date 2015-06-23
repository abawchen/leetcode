import unittest
import sys
sys.path.append('./')
solutions = __import__('solutions.168_excel_sheet_column_title', fromlist='*')


class Test(unittest.TestCase):

    def test_convertToTitle(self):
        s = solutions.Solution()

        self.assertEqual(s.convertToTitle(1), "A")
        self.assertEqual(s.convertToTitle(2), "B")
        self.assertEqual(s.convertToTitle(26), "Z")
        
        self.assertEqual(s.convertToTitle(27), "AA")
        self.assertEqual(s.convertToTitle(28), "AB")
        self.assertEqual(s.convertToTitle(53), "BA")
        self.assertEqual(s.convertToTitle(676), "YZ")
        self.assertEqual(s.convertToTitle(702), "ZZ")

        self.assertEqual(s.convertToTitle(703), "AAA")
        self.assertEqual(s.convertToTitle(704), "AAB")
        self.assertEqual(s.convertToTitle(728), "AAZ")


        self.assertEqual(s.convertToTitle(729), "ABA")
        self.assertEqual(s.convertToTitle(1403), "BAY")
        self.assertEqual(s.convertToTitle(5372), "GXP")


if __name__ == '__main__':
    unittest.main()
