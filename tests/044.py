import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.044_wildcard_matching', fromlist='*')


class Test(unittest.TestCase):

    def test_isMatching(self):
        s = solutions.Solution()

        # st, pa = "aa", "a"
        # self.assertEqual(s.isMatch(st, pa), False)

        # st, pa = "aa", "aa"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "aaa", "aa"
        # self.assertEqual(s.isMatch(st, pa), False)

        # st, pa = "aa", "*"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "aa", "a*"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "aaa", "a*"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "aa", "?*"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "aab", "c*a*b"
        # self.assertEqual(s.isMatch(st, pa), False)

        # st, pa = "aabefefefb", "*?*?"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "aabefefefb", "*b*?"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "", "*?"
        # self.assertEqual(s.isMatch(st, pa), False)

        # st, pa = "aabefefefb", "*b*b"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "aabefefefba", "*b*a*"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "a", "*a*"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "", "*"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "aabefbcefefb", "*b*bc*"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "ababcefbefefbc", "*b*bc*"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "aabefefefb", "*b*a"
        # self.assertEqual(s.isMatch(st, pa), False)

        # st, pa = "aabefefefba", "*b*a"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "aabefefefb", "*b"
        # self.assertEqual(s.isMatch(st, pa), True)

        # st, pa = "aabefefefbe", "*b?"
        # self.assertEqual(s.isMatch(st, pa), True)


        # st, pa = "aabefbcefefb", "*b*bc*f*ef?b"
        # self.assertEqual(s.isMatch(st, pa), False)

        # st, pa = "fe", ""
        # self.assertEqual(s.isMatch(st, pa), False)

        st = "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb"
        pa = "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**" 
        self.assertEqual(s.isMatch(st, pa), True)

if __name__ == '__main__':
    unittest.main()
