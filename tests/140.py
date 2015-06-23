import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.140_word_break_ii', fromlist='*')


class Test(unittest.TestCase):

    def test_wordBreak(self):
        s = solutions.Solution()

        st = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict = {"a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"}
        self.assertEqual(s.wordBreak(st, wordDict), [])


        st, wordDict = "leetcode", ["leet", "code"]
        self.assertEqual(s.wordBreak(st, wordDict), ["leet code"])

        st, wordDict = "catsanddog", ["cat", "cats", "and", "sand", "dog"]
        self.assertEqual(s.wordBreak(st, wordDict), ['cats and dog', 'cat sand dog'])

        st, wordDict = "aaaaaaa", ["aaa", "aaaa", "a"]
        self.assertEqual(
            set(s.wordBreak(st, wordDict)), 
            set(['aaa aaaa', 'a a a aaaa', 'aaaa aaa', 'a aaa aaa', 'aaa a aaa', 'a a a a aaa', 'a a aaaa a', 'aaa aaa a', 'a a a aaa a', 'a aaaa a a', 'a a aaa a a', 'aaaa a a a', 'a aaa a a a', 'aaa a a a a', 'a a a a a a a']))


if __name__ == '__main__':
    unittest.main()
