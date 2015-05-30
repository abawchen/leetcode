# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 2, a solution set is:
# "(())", "()()"

# For example, given n = 3, a solution set is:
# "((()))", "(()())", "(())()", "()(())", "()()()" 

# For example, given n = 4, a solution set is:
# "(((())))", "((()()))", "((())())", "(()(()))", "(()()())" 
# 


class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n is 0:
            return []

        parentheses = []
        stack = [('(', 1, (n-1))]
        while stack:
            (parenthes, cur, left) = stack.pop()

            if left == 0:
                parentheses.append(parenthes + (')'*cur))
            else:
                if cur > 0:
                    stack.append((parenthes + ')', cur-1, left))
                stack.append((parenthes + '(', cur+1, left-1))

        
        return parentheses


        