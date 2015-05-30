import unittest
import sys
sys.path.append('./')

# http://stackoverflow.com/questions/147507/how-does-one-do-the-equivalent-of-import-from-module-with-pythons-import
solutions = __import__('solutions.022_generate_parentheses', fromlist='*')


class Test022(unittest.TestCase):

    def test_generateParenthesis(self):
        s = solutions.Solution()

        self.assertEqual(s.generateParenthesis(0), [])
        self.assertEqual(s.generateParenthesis(1), ["()"])
        self.assertEqual(s.generateParenthesis(2), ["(())", "()()"])
        self.assertEqual(s.generateParenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])


if __name__ == '__main__':
    unittest.main()
