import time
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# Your algorithm should run in O(n) complexity. 

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        # http://stackoverflow.com/questions/4576115/python-list-to-dictionary
        self.dic = dict((n, n) for n in nums)
        self.dup = dict(self.dic)

        longest = 1
        for key in self.dup:
            if self.dic.has_key(key):
                local = 1
                local += (self.check(key+1, 1) + self.check(key-1, -1))
            longest = max(longest, local)

        return longest

    def check(self, key, i):
        n = 0
        while self.dic.has_key(key):
            self.dic.pop(key)
            n += 1
            key += i
        return n

s = Solution()
# print s.longestConsecutive([100])
print s.longestConsecutive([0, -1]) #2
print s.longestConsecutive([1, 2]) #2
print s.longestConsecutive([100, 100, 101]) #2
print s.longestConsecutive([102, 100, 100, 101]) #3
print s.longestConsecutive([100, 4, 200, 1, 3, 2]) #4
print s.longestConsecutive([100, 4, 1, 3, 2, 145, 146, 148, 147, 144, 300, 150, 149]) #7
print s.longestConsecutive([193, 100, 4, 200, 1, 3, 2, 195, 196, 198, 197, 194, 300, 150]) #6
print s.longestConsecutive([193, 100, 4, 200, 1, 3, 2, 195, 196, 198, 197, 194, 300, 150, 299, 298, 297, 296, 295, 294, 293]) #8

start_time = time.time()
print s.longestConsecutive([2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645]) #3
print("--- %s seconds ---" % (time.time() - start_time))