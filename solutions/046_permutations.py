# Given a collection of numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1]. 

# [1,2] have the following permutations:
# [1,2], [2,1]


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):

        # stack version(1):
        ans = []
        stack = [([], nums)]
        while stack:
            ret, nums = stack.pop(0)
            if nums:
                for i in range(len(nums)):
                    stack.append((ret + [nums[i]], nums[:i] + nums[i+1:]))
            else:
                ans.append(ret)
        return ans


        # stack version(2):
        # if not nums:
        #     return nums

        # res = [[nums[0]]]
        # for i in range(1, len(nums)):
        #     for j in range(len(res)):
        #         tmp = res.pop(0)
        #         for k in range(len(tmp)+ 1):
        #             res.append(tmp[:k] + [nums[i]] + tmp[k:])

        # return res



        # recursion version:
        # if len(nums) <= 1:
        #     return [nums]

        # permutations = []
        # for i in range(len(nums)):
        #     permutations.extend([ [nums[i]] + p for p in self.permute(nums[:i] + nums[i+1:]) ])

        # return permutations
