# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# For example,
# Given input array nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length. 


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):

        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)


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