import unittest
import sys
sys.path.append('./')
solutions = __import__('solutions.125_valid_palindrome', fromlist='*')
utils = __import__('utils.interval', fromlist='*')


class Test125(unittest.TestCase):

    def test_isPalindrome(self):
        s = solutions.Solution()

        self.assertTrue(
            s.isPalindrome("A man, a plan, a canal: Panama")
        )

        self.assertFalse(
            s.isPalindrome("race a car")
        )


        self.assertTrue(
            s.isPalindrome("A man, a plan, a canal: Panama 123")
        )

        self.assertTrue(
            s.isPalindrome(" ")
        )

        self.assertTrue(
            s.isPalindrome("")
        )

if __name__ == '__main__':
    unittest.main()