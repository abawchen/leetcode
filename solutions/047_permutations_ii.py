# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1]. 


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        if not nums:
            return nums

        res = {(nums[0],)}
        for i in range(1, len(nums)):
            tmp = set()
            while res:
                base = res.pop()
                for j in range(len(base)+ 1):
                    tmp.add(tuple(base[:j]) + (nums[i],) + tuple(base[j:]))
            res = tmp

        return [ list(t) for t in res ]
        
        # dic = {str([nums[0]]):1}
        # res = [[nums[0]]]
        # for i in range(1, len(nums)):
        #     for j in range(len(res)):
        #         base = res.pop(0)
        #         dic.pop(str(base))
        #         for k in range(len(base)+ 1):
        #             tmp = base[:k] + [nums[i]] + base[k:]
        #             if str(tmp) not in dic:
        #                 res.append(base[:k] + [nums[i]] + base[k:])
        #                 dic[str(tmp)] = 1

        # return res