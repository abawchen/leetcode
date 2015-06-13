# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 

# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.


class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        from string import ascii_uppercase
        n -= 1
        quotient, title = n/26, ""
        while quotient > 26:
            quotient -= 1
            quotient, remainer = quotient/26, quotient%26
            title = ascii_uppercase[remainer] + title

        if quotient > 0:
            title = ascii_uppercase[quotient-1] + title

        title += ascii_uppercase[n%26]

        return title