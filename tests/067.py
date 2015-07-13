import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.067_add_binary', fromlist='*')


class Test(unittest.TestCase):


    def test_addBinary(self):

        s = solutions.Solution()

        a, b = "1", "11"
        expected = "100"
        self.assertEqual(s.addBinary(a, b), expected)


        a, b = "11", "11"
        expected = "110"
        self.assertEqual(s.addBinary(a, b), expected)


        a, b = "111110", "1"
        expected = "111111"
        self.assertEqual(s.addBinary(a, b), expected)


if __name__ == '__main__':
    unittest.main()
