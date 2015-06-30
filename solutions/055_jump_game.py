# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false. 

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):

        maximum = 0
        for i, n in enumerate(nums):
            if maximum < i:
                return False
            elif maximum >= len(nums)-1:
                return True

            maximum = max(maximum, i+n)

        # maximum = -1
        # stack = [0]
        # while stack:
        #     idx = stack.pop()

        #     if idx == len(nums)-1:
        #         return True

        #     for step in range(nums[idx], 0, -1):
        #         next = idx + step

        #         if next >= len(nums)-1:
        #             return True

        #         possible = next + nums[next]
        #         if possible > maximum:
        #             maximum = possible
        #             stack.append(next)

        # return False
