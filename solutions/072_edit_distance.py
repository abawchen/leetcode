# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

# You have the following 3 operations permitted on a word:

# a) Insert a character
# b) Delete a character
# c) Replace a character

class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):

        m = [[0 for i in xrange(len(word2)+1)] for i in xrange(len(word1)+1)]
        for i in range(1, len(word1)+1):
            m[i][0] = i

        for j in range(1, len(word2)+1):
            m[0][j] = j

        for i in xrange(1, len(word1)+1):
            for j in xrange(1, len(word2)+1):
                m[i][j] = min(
                    m[i-1][j-1] + int(word1[i-1] != word2[j-1]),
                    m[i-1][j] + 1,
                    m[i][j-1] + 1)

        return m[-1][-1]

        # from collections import defaultdict
        # minDic = defaultdict(int)

        # for i in range(1, len(word1)+1):
        #     minDic[(i, 0)] = i

        # for j in range(1, len(word2)+1):
        #     minDic[(0, j)] = j

        # for i in xrange(1, len(word1)+1):
        #     for j in xrange(1, len(word2)+1):
        #         minDic[(i, j)] = min(
        #             minDic[(i-1, j-1)] + int(word1[i-1] != word2[j-1]),
        #             minDic[(i-1, j)] + 1,
        #             minDic[(i, j-1)] + 1)

        # return minDic[(len(word1), len(word2))]