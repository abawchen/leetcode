# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome. 


class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s = ''.join([c for c in s.lower() if c.isalnum()])
        if not s:
            return True
        
        start, end = 0, len(s)-1
        while start <= end:
            if s[start] != s[end]:
                return False
            start, end = start+1, end-1

        return True
