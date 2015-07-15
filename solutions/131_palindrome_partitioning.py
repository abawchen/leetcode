# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return 

# [
#   ["aa","b"],
#   ["a","a","b"]
# ]


class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        partitions = []
        self._partition(s, partitions)
        return partitions

    def _partition(self, s, partitions, tmp=[]):
        
        if len(s) <= 1:
            partitions.append((tmp + [s]) if s else tmp[:])

        else:
            for i in xrange(len(s)):
                if self._isPalindrome(s[:i+1]):
                    tmp.append(s[:i+1])
                    self._partition(s[i+1:], partitions, tmp)
                    tmp.pop()

    def _isPalindrome(self, s):

        start, end = 0, len(s)-1
        while start <= end and s[start] == s[end]:
            start += 1
            end -= 1

        return start >= end