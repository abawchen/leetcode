# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# For example,

#     Given numerator = 1, denominator = 2, return "0.5".
#     Given numerator = 2, denominator = 1, return "2".
#     Given numerator = 2, denominator = 3, return "0.(6)".

# Credits:
# Special thanks to @Shangrila for adding this problem and creating all test cases.


class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        import operator

        isNegtive = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        quotient = int(operator.truediv(numerator, denominator))
        remainder = numerator % denominator
        dic = {remainder:0}
        intPart = "-" + str(quotient) if isNegtive else str(quotient)
        decimals = ""
        idx = 1
        while remainder != 0:
            # print "abaw"
            numerator = remainder * 10
            quotient = int(operator.truediv(numerator, denominator))
            remainder = numerator % denominator
            decimals += str(quotient)
            if remainder in dic:
                decimals = decimals[:dic[remainder]] + "("+decimals[dic[remainder]:]+")"
                break

            dic[remainder] = idx
            idx += 1

        return intPart+"."+decimals if len(decimals) else intPart

s = Solution()
print s.fractionToDecimal(2, 1)
print s.fractionToDecimal(1, 2)
print s.fractionToDecimal(2, 3)
print s.fractionToDecimal(100, 11) #9.(09)
print s.fractionToDecimal(10, 23) #0.(4347826086956521739130)
print s.fractionToDecimal(165, 81) #2.(037)
print s.fractionToDecimal(1, 333)
print s.fractionToDecimal(-2147483648, 1)
print s.fractionToDecimal(50, 8)
print s.fractionToDecimal(1, 6)
print s.fractionToDecimal(-50, 8)
print s.fractionToDecimal(-1, 333)
print s.fractionToDecimal(-1, 6)
print s.fractionToDecimal(-1, -6)
print s.fractionToDecimal(1, -6)

# print s.fractionToDecimal(-1, 2147483647) #????

# test cases

# https://leetcode.com/discuss/20346/165-81-2-0-370-or-2-037
# 165/81=2.(037)

# https://leetcode.com/discuss/26306/this-online-judge-question-is-not-reasonable
# 10/23 = 0.(43478260869565521739130)


# https://leetcode.com/discuss/28804/result-of-test-case-1-214748364-should-be-repeating-decimal


# https://leetcode.com/discuss/19247/a-question-for-the-cases-to-be-used-to-judge-the-submit
# 1/-2147483647 = ???