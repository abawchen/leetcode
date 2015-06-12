# You are given a string, s, and a list of words, words, that are all of the same length.
# Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]

# You should return the indices: [0,9].
# (order does not matter). 


class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        # print (len(s), len(words))
        
        indices = []
        length = len(words[0])
        for i in range(len(s)):
            j, k, used = i, i, set()
            while s[j:j+length] in words and s[j:j+length+1] not in used:
                used.add(s[j:j+length])
                j += length
            if len(used) == len(words):
                indices.append(k)

        return indices


