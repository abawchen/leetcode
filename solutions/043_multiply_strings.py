# Given two numbers represented as strings, return multiplication of the numbers as a string.

# Note: The numbers can be arbitrarily large and are non-negative.


class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):

        ans = [0] * (len(num1)+len(num2))
        for i1, n1 in enumerate(reversed(num1)):
            vals = [0] * len(num2)
            for i2, n2 in enumerate(reversed(num2)):
                vals[i2] = int(n1)*int(n2)
            
            for i, val in enumerate(vals):
                v = val+ans[i1+i]
                ans[i1+i]= v%10
                ans[i1+i+1] += v/10

        ans = ''.join(str(n) for n in reversed(ans)).lstrip("0")
        return ans if ans else "0"