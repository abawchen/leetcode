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
        cur, op = 0, "+"

        def cal(op, cur):
            if op == "+":
                stack.append(cur)
            elif op == "-":
                stack.append(-cur)
            elif op == "*":
                stack.append(stack.pop()*cur)
            elif op == "/":
                stack.append(int(stack.pop()/cur))

        for c in s:
            if c.isdigit():
                cur = cur*10 + int(c)
            elif c in ops:
                cal(op, cur)
                cur, op = 0, c
            elif c == "(":
                stack.append(op)
                stack.append(c)
                op = "+"
            elif c == ")":
                # calcuate the result in current `()`
                cal(op, cur)
                cur = 0

                # ver #1
                while stack[-1] != "(":
                    cur += stack.pop()

                # pop `(`
                stack.pop()

                # ver #2
                # v = stack.pop()
                # while v != "(":
                #     cur += v
                #     v = stack.pop()

                # get the operator(sign) before `()`
                op = stack.pop()

        cal(op, cur)
        return sum(stack)

    # recursive version
    # def calculate(self, s: str) -> int:

    #     def inner(i):
    #         stack, cur, op = [], 0, "+"

    #         def cal(op, cur):
    #             if op == "+":
    #                 stack.append(cur)
    #             elif op == "-":
    #                 stack.append(-cur)
    #             elif op == "*":
    #                 stack.append(stack.pop()*cur)
    #             elif op == "/":
    #                 stack.append(int(stack.pop()/cur))

    #         while i < len(s):
    #             if s[i].isdigit():
    #                 cur = cur*10 + int(s[i])
    #             elif s[i] in "+-*/":
    #                 cal(op, cur)
    #                 cur, op = 0, s[i]
    #             elif s[i] == "(":
    #                 cur, i = inner(i+1)
    #             elif s[i] == ")":
    #                 cal(op, cur)
    #                 return sum(stack), i
    #             i += 1
    #         cal(op, cur)
    #         return sum(stack)

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

    def test_05(self):
        s = "3+2*2"
        got = self.solution.calculate(s)
        expected = eval(s)
        self.assertEqual(expected, got)

    def test_06(self):
        s = " 3/2 "
        got = self.solution.calculate(s)
        expected = int(eval(s))
        self.assertEqual(expected, got)

    def test_06(self):
        s = " 3+5 / 2 "
        got = self.solution.calculate(s)
        expected = int(eval(s))
        self.assertEqual(expected, got)

    def test_07(self):
        s = " 3+500 / (1+2*3*(2+9/3)) "
        got = self.solution.calculate(s)
        expected = int(eval(s))
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
