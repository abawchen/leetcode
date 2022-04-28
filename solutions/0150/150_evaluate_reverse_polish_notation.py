class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        import operator
        stack = []
        ops = {
            '+': operator.add, '-': operator.sub,
            '*': operator.mul, '/': operator.truediv
        }

        for t in tokens:
            if t in ops:
                a, b = stack.pop(), stack.pop()
                stack.append(int(ops[t](b, a)))
            else:
                stack.append(int(t))

        return stack.pop()


s = Solution()

# print(s.evalRPN(["3","-4","+"]))
# print(s.evalRPN(["2", "1", "+", "3", "*"]))
# print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# print(s.evalRPN(["5","1","2","+","4","*","+","3","-"]))
# print(s.evalRPN(["4","-2","/","2","-3","-","-"]))