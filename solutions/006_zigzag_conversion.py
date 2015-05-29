class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows <= 1:
            return s

        r = 0
        i = 1
        # http://stackoverflow.com/questions/1154494/python-list-initialization-differences
        zigzag = [[] for n in range(numRows)]
        
        for c in s:
            zigzag[r].append(c)
            r += i
            if r == numRows:
                i = -1
                r = numRows - 2
            elif r == -1:
                i = 1
                r = 1

        # http://stackoverflow.com/questions/103844/how-do-i-merge-a-2d-array-in-python-into-one-string-with-list-comprehension
        return ''.join(item for innerlist in zigzag for item in innerlist)


s = Solution()
print s.convert("PAYPALISHIRING", 3)
print s.convert("Q123", 3)
print s.convert("Q123", 2)
print s.convert("Q123", 1)
print s.convert("Q123", 0)
# PAHNAPLSIIGYIR

# l = []
# for i in xrange(1, numRows-1):
#     l.append((2*(numRows-(i+1)), 2*i))

# index = {}
# zigzag = [[]] * numRows
# x = 1
# for i in xrange(len(s)):
#     r = i % numRows
#     zigzag[r].append(s[index.get(r, r)])
#     if r == 0 or r == (numRows-1):
#         index[r] += 2 * (numRows-1)
#     else:
#         index[r] += 
