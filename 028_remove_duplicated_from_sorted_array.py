# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# For example,
# Given input array nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length. 


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):

        # O(n?)
        if not nums:
            return 0

        tail = 0
        for i in xrange(1, len(nums)):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]

        return tail + 1

        # # O(n?)
        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i] == nums[i+1]:
        #         del nums[i]
        #     else:
        #         i += 1
        # return len(nums)

        # WA
        # nums[:] = list(set(nums))
        # return len(nums)

import time
start_time = time.time()

s = Solution()
print s.removeDuplicates([])
print s.removeDuplicates([1])
print s.removeDuplicates([1, 1, 1])
print s.removeDuplicates([1, 2])
print s.removeDuplicates([1, 1, 2])
print s.removeDuplicates([1, 1, 2, 2])
print s.removeDuplicates([1, 1, 2, 2, 2, 2, 3])
print s.removeDuplicates([0, 1, 1, 2, 2, 2, 2, 3])
print s.removeDuplicates([0, 0, 1, 1, 2, 2, 2, 2, 3, 8])
print s.removeDuplicates([0, 0, 1, 1, 2, 2, 2, 2, 3, 8, 9, 9, 10, 10])

print("--- %s seconds ---" % (time.time() - start_time))