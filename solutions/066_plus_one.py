# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        
        ans = []
        i, plus = 0, 1
        for digit in reversed(digits):
            ans.insert(0, (digit + plus) % 10)
            plus = int(digit == 9 and plus == 1)

            if plus == 0:
                ans = digits[:-i-1] + ans
                break

            i += 1

        if plus == 1:
            ans.insert(0, 1)

        return ans
