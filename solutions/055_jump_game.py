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

        stack = [0]
        visited = {0}
        while stack:
            idx = stack.pop()

            if idx == len(nums)-1:
                return True

            for s in range(1, nums[idx]+1):
                if idx+s not in visited and idx+s < len(nums):
                    stack.append(idx+s)
                    visited.add(idx+s)

        return False


