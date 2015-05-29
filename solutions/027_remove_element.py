# Given an array and a value, remove all instances of that value in place and return the new length.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length. 

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):

        nums[:] = filter(lambda x: x != val, nums)
        return len(nums)

        # or 
        # for n in list(nums):
        #     if n == val:
        #         nums.remove(n)
        # return len(nums)

import time
start_time = time.time()

s = Solution()
print s.removeElement([], 1)
print s.removeElement([1, 1, 2, 1, 1], 1)

print("--- %s seconds ---" % (time.time() - start_time))

# print s.removeElement(None, 1)