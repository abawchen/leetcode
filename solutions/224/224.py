import unittest

"""
Given a string s representing a valid expression,
implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().
"""


class Solution:
    
    # non-recursive version
    def calculate(self, s: str) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        ans, cur, op = 0, 0, "+"

        def cal(ans, op, cur):
            if op == "+":
                return ans+cur
            elif op == "-":
                return ans-cur

        for c in s:
            if c.isdigit():
                cur = cur*10 + int(c)
            elif c in ops:
                ans = cal(ans, op, cur)
                cur, op = 0, c
            elif c == "(":
                stack.append(ans)
                stack.append(op)
                ans, op = 0, "+"
            elif c == ")":
                # calcuate the result in current `()`
                ans = cal(ans, op, cur)

                # take care the operator(sign) before `()`
                ans = cal(0, stack.pop(), ans)

                # sum with the ans before `()`
                ans += stack.pop()

                cur = 0

        ans = cal(ans, op, cur)
        return ans

    # recursive version
    # def calculate(self, s: str) -> int:

    #     def inner(i):
    #         ans, cur, op = 0, 0, "+"

    #         def cal(ans, op, cur):
    #             if op == "+":
    #                 ans += cur
    #             elif op == "-":
    #                 ans -= cur
    #             return ans

    #         while i < len(s):
    #             if s[i].isdigit():
    #                 cur = cur*10 + int(s[i])
    #             elif c in "+-*/":
    #                 ans = cal(ans, op, cur)
    #                 cur = 0
    #                 op = s[i]
    #             elif c == "(":
    #                 cur, i = inner(i+1)
    #             elif c == ")":
    #                 ans = cal(ans, op, cur)
    #                 return ans, i
    #             i += 1
    #         ans = cal(ans, op, cur)
    #         return ans

    #     return inner(0)


class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_01(self):
        s = "1 + 1"
        got = self.solution.calculate(s)
        expected = eval(s)
        self.assertEqual(expected, got)

    def test_02(self):
        s = " 2-1 + 2 "
        got = self.solution.calculate(s)
        expected = eval(s)
        self.assertEqual(expected, got)

    def test_03(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        got = self.solution.calculate(s)
        expected = eval(s)
        self.assertEqual(expected, got)

    def test_04(self):
        s = "-(3+1)"
        got = self.solution.calculate(s)
        expected = eval(s)
        self.assertEqual(expected, got)

if __name__ == '__main__':
    unittest.main()
