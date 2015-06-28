import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.044_wildcard_matching', fromlist='*')


class Test(unittest.TestCase):

    def test_isMatching(self):
        s = solutions.Solution()

        st, pa = "aaa", "ab*a*c*a"
        self.assertEqual(s.isMatch(st, pa), False)

        st, pa = "aa", "a"
        self.assertEqual(s.isMatch(st, pa), False)

        st, pa = "aa", "aa"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aaa", "aa"
        self.assertEqual(s.isMatch(st, pa), False)

        st, pa = "aba", "ab"
        self.assertEqual(s.isMatch(st, pa), False)

        st = "abaaab"
        pa = "*a*aab"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aa", "*"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aa", "a*"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aaa", "a*"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aa", "?*"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aab", "c*a*b"
        self.assertEqual(s.isMatch(st, pa), False)

        st, pa = "aabefefefb", "*?*?"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aa", "*?*?"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aaa", "*?*?"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "a", "*?*?"
        self.assertEqual(s.isMatch(st, pa), False)

        st, pa = "a", "*?*"
        self.assertEqual(s.isMatch(st, pa), True)


        st, pa = "aabefefefb", "*b*?"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "", "*?"
        self.assertEqual(s.isMatch(st, pa), False)

        st, pa = "", "*"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aabefefefb", "*b"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aabefefefb", "*b*b"
        self.assertEqual(s.isMatch(st, pa), True)

        
        st, pa = "aab", "*b*a*"
        self.assertEqual(s.isMatch(st, pa), False)

        st, pa = "aab", "*b*a"
        self.assertEqual(s.isMatch(st, pa), False)

        st, pa = "aabefefefba", "*b*a*"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "a", "*a*"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "", "*"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aabefbcefefb", "*b*bc*"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "ababcefbefefbc", "*b*bc*"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aabefefefb", "*b*a"
        self.assertEqual(s.isMatch(st, pa), False)

        st, pa = "efefefb", "*a"
        self.assertEqual(s.isMatch(st, pa), False)

        st, pa = "aabefefefba", "*b*a"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aabaefefefba", "*ba"
        self.assertEqual(s.isMatch(st, pa), True)
        
        st, pa = "aefefefba", "a"
        self.assertEqual(s.isMatch(st, pa), False)


        st, pa = "aabefefefb", "*b"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "", ""
        self.assertEqual(s.isMatch(st, pa), True)        

        st, pa = "efefefb", ""
        self.assertEqual(s.isMatch(st, pa), False)

        st, pa = "aabefefefbe", "*b?"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = "aabefbcefefb", "*b*bc*f*ef?b"
        self.assertEqual(s.isMatch(st, pa), False)

        st, pa = "fe", ""
        self.assertEqual(s.isMatch(st, pa), False)

        # suitable for shortest
        st = "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb"
        pa = "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"
        # pa = '*b*a*a*b*b*a*b*bbb*baa*bba*b*bb*b*a*aab*a*'
        self.assertEqual(s.isMatch(st, pa), True)


        st = "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbb"
        pa = "*b*a*a*b*b*a*b*bbb*baa*bba*b*bb*b*a*" #36
        self.assertEqual(s.isMatch(st, pa), True)

        st = "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaab"
        pa = "*b*a*a*b*b*a*b*bbb*baa*bba*b*bb*b*a*aab"
        self.assertEqual(s.isMatch(st, pa), True)

        st = "abaaab"
        pa = "*a*aab"
        self.assertEqual(s.isMatch(st, pa), True)

        st = "abbaa"
        pa = "*b*a*a*"
        self.assertEqual(s.isMatch(st, pa), True)

        st, pa = ('b', 'bb*baa*bba*b*bb*b*a*aab*a*')
        self.assertEqual(s.isMatch(st, pa), False)


        # suitable for longest
        st = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
        # # pa = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
        sp = "b*bb*a*bba*b*a*bbb*aba*babbb*aa*aabb*bbb*a"
        self.assertEqual(s.isMatch(st, pa), False)



if __name__ == '__main__':
    unittest.main()
