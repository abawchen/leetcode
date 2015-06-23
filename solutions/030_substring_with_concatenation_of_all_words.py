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
    # O(mn)
    def findSubstring(self, s, words):        
        from collections import defaultdict

        indices, wordsDic = [], defaultdict(int)
        sl, wl, twl, total = len(s), len(words[0]), len(words[0])*len(words), len(words)

        for w in words:
            wordsDic[w] += 1

        for i in range(sl):
            t, j, dic = 0, i, wordsDic.copy()

            if twl > sl-i:
                return indices

            while dic[s[j:j+wl]] > 0:
                dic[s[j:j+wl]] -= 1
                t, j = t+1, j+wl

            if t == total:
                indices.append(i)

        return indices


