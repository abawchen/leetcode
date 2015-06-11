# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT. 


class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):

        isNeg = False
        if dividend < 0:
            dividend = -dividend
            isNeg = not isNeg
        if divisor < 0:
            divisor = -divisor
            isNeg = not isNeg

        i, quotient, base, divisors = 0, 0, [1], [divisor]
        while dividend >= divisors[i]:
            dividend -= divisors[i]
            divisors.append(divisors[i]+divisors[i])
            base.append(base[i]+base[i])
            quotient, i = quotient+base[i], i+1

        for j in xrange(i-1, -1, -1):
            if dividend >= divisors[j]:
                dividend -= divisors[j]
                quotient += base[j]

        quotient = -quotient if isNeg else quotient

        return 2147483647 if quotient > 2147483647 or quotient < -2147483748 else quotient

