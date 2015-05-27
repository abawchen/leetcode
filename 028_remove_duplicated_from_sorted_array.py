# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# For example,
# Given input array nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length. 


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        nums[:] = self.remove(nums)
        print nums
        return len(nums)

    def remove(self, nums):
        if len(nums) <= 1:
            return nums

        for i in xrange(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[:i] + self.remove(nums[i+1:])

        return nums

s = Solution()
print s.removeDuplicates([])
print s.removeDuplicates([1])
print s.removeDuplicates([1, 2])
print s.removeDuplicates([1, 1, 2])
print s.removeDuplicates([1, 1, 2, 2])
print s.removeDuplicates([1, 1, 2, 2, 2, 2, 3])
print s.removeDuplicates([0, 1, 1, 2, 2, 2, 2, 3])
print s.removeDuplicates([0, 0, 1, 1, 2, 2, 2, 2, 3, 8])
print s.removeDuplicates([0, 0, 1, 1, 2, 2, 2, 2, 3, 8, 9, 9, 10, 10])