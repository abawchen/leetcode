import unittest
import sys
sys.path.append('./')


solutions = __import__('solutions.032_longest_valid_parentheses', fromlist='*')


class Test032(unittest.TestCase):

    def test_longestValidParentheses(self):
        s = solutions.Solution()

        self.assertEqual(
            s.longestValidParentheses("()(()"),
            2)

        self.assertEqual(
            s.longestValidParentheses(")()())"),
            4)

        self.assertEqual(
            s.longestValidParentheses("(()"),
            2)


        self.assertEqual(
            s.longestValidParentheses(""),
            0)

        self.assertEqual(
            s.longestValidParentheses(")"),
            0)

        self.assertEqual(
            s.longestValidParentheses(")("),
            0)

        self.assertEqual(
            s.longestValidParentheses("()"),
            2)

        self.assertEqual(
            s.longestValidParentheses("()()()"),
            6)

        self.assertEqual(
            s.longestValidParentheses("((()))()()"),
            10)

        self.assertEqual(
            s.longestValidParentheses("()()())((()))()()"),
            10)

        self.assertEqual(
            s.longestValidParentheses("((()))()()((((((((((())))))))))()()"),
            24)

if __name__ == '__main__':
    unittest.main()