import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.014_longest_common_prefix', fromlist='*')


class Test012(unittest.TestCase):

    def test_longestCommonPrefix(self):
        s = solutions.Solution()

        self.assertEqual(
            s.longestCommonPrefix(["abcde", "abc", "ab"]), "ab")

        self.assertEqual(
            s.longestCommonPrefix(["123456", "123", "456"]), "")

        self.assertEqual(
            s.longestCommonPrefix([""]), "")

        self.assertEqual(
            s.longestCommonPrefix([]), "")
        
if __name__ == '__main__':
    unittest.main()
