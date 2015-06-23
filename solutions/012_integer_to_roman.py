# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        normalDic = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }
        specialDic = {
            '41': 'IV', # 4
            '91': 'IX', # 9
            '42': 'XL', # 40
            '92': 'XC', # 90
            '43': 'CD', # 400
            '93': 'CM', # 900
        }

        roman = ""
        remainders = ['4', '9']
        divisors = [1000, 500, 100, 50, 10, 5, 1]
        for i, divisor in enumerate(divisors):
            quotient = num/divisor
            if quotient > 0:
                roman += normalDic[divisor] * quotient
            num = num % divisor

            if str(num)[0] in remainders:
                roman += specialDic[str(num)[0] + str(len(str(num)))]
                num -= int(str(num)[0]) * (10 ** (len(str(num)) - 1))

        return roman