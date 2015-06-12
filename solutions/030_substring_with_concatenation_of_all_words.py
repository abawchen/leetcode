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
        # from collections import defaultdict
        # dic = defaultdict(list)

        # indices, length, totalLength = [], len(words[0]), len(words[0])*len(words)
        # for i in range(len(s)):
        #     j, k, dupWords = i, i, words[:]

        #     if totalLength > len(s[j:]):
        #         # print "dic:", dic
        #         return indices

        #     if j in dic:
        #         for w in dic[j]:
        #             print "w:", w
        #             # j += len(w)
        #             dupWords.remove(w)
        #         print "(j, dic[j]):", (j, dic[j])

        #     while s[j:j+length] in dupWords:
        #         # print "(i, j):", (i, j)
        #         if dic[j+length]:
        #             dic[j+length] += dic[j]
        #         else:
        #             dic[j+length] += [s[j:j+length]]
        #         dupWords.remove(s[j:j+length])
        #         j += length

        #     print "(i, dupWords):", (i, dupWords)
        #     if not dupWords:
        #         # print "new k:", k
        #         indices.append(k)


        # brute force
        # print (len(s), len(words))
        # print words
        indices, failed = [], set()
        length, totalLength = len(words[0]), len(words[0])*len(words)
        for i in range(len(s)):
            j, dupWords = i, words[:]

            if totalLength > len(s[j:]):
                return indices

            if s[i:i+totalLength] in failed:
                continue

            while s[j:j+length] in dupWords:
                dupWords.remove(s[j:j+length])
                j += length

            if not dupWords:
                indices.append(i)
            else:
                failed.add(s[i:i+totalLength])

        return indices


