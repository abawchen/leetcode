import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.076_minimum_window_substring', fromlist='*')


class Test(unittest.TestCase):


    def test_minWindow(self):

        s = solutions.Solution()

        S, T = "ADOBECODEBANC", "ABC"
        expected = "BANC"
        self.assertEqual(s.minWindow(S, T), expected)

        S, T = "A", "AA"
        expected = ""
        self.assertEqual(s.minWindow(S, T), expected)


        S, T = "bba", "ab"
        expected = "ba"
        self.assertEqual(s.minWindow(S, T), expected)

        S, T = "aa", "aa"
        expected = "aa"
        self.assertEqual(s.minWindow(S, T), expected)

        S, T = "adobecodebanc", "abcda"
        expected = "adobecodeba"
        self.assertEqual(s.minWindow(S, T), expected)


if __name__ == '__main__':
    unittest.main()
