# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.


class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        romanDic = {
            'M': 1000, 'CM': 900,
            'D': 500,  'CD': 400,
            'C': 100,  'XC': 90,
            'L': 50,   'XL': 40,
            'X': 10,   'IX': 9,
            'V': 5,    'IV': 4,
            'I': 1
        }

        num, i = 0, 0
        while i < len(s)-1:
            if s[i:i+2] in romanDic:
                num += romanDic[s[i:i+2]]
                i += 2
            else:
                num += romanDic[s[i]]
                i += 1
        if i < len(s):
            num += romanDic[s[-1]]
        return num