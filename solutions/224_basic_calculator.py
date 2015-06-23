# Implement a basic calculator to evaluate a simple expression string.

# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

# You may assume that the given expression is always valid.

# Some examples:

# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23

# Note: Do not use the eval built-in library function. 

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        self.SIGN = {'+': 1, '-': -1}
        return self._calcuate(s.replace(" ", ""), 0)[1]
        
    def _calcuate(self, s, i):
        val = 0
        
        while i < len(s):
            if s[i] in self.SIGN:
                sign, i = self.SIGN[s[i]], i+1
                if s[i] == '(':
                    i, tmp = self._calcuate(s, i+1)
                else:
                    tmp = 0
                    while i < len(s) and s[i].isdigit():
                        tmp, i = tmp*10 + int(s[i]), i+1
                val += sign*tmp
            elif s[i].isdigit():
                val, i = val*10 + int(s[i]), i+1
            elif s[i] == '(':
                i, val = self._calcuate(s, i+1) 
            else:
                return i+1, val

        return i, val
