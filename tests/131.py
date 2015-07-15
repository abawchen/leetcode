import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.131_palindrome_partitioning', fromlist='*')


class Test(unittest.TestCase):

    def test_partition(self):
        s = solutions.Solution()

        st = "aab"
        expected = [["aa", "b"], ["a", "a", "b"]]
        self.assertEqual(sorted(s.partition(st)), sorted(expected))

        st = "aba"
        expected = [["a", "b", "a"], ["aba"]]
        self.assertEqual(sorted(s.partition(st)), sorted(expected))

        st = "aaba"
        expected = [["aa", "b", "a"], ["a", "a", "b", "a"], ["a", "aba"]]
        self.assertEqual(sorted(s.partition(st)), sorted(expected))


        st = ""
        expected = [[]]
        self.assertEqual(sorted(s.partition(st)), sorted(expected))


        
if __name__ == '__main__':
    unittest.main()
