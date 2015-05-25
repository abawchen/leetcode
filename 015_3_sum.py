# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# Note:
#     Elements in a triplet (a,b,c) must be in non-descending order.
#     The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},
#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if not nums or len(nums) <= 2:
            return []

        idx = -1
        dic = {}
        sets = []
        nums = sorted(nums)
        for i, n in enumerate(nums):
            if n >= 0 and idx == -1:
                idx = i
            dic[n] = dic.get(n, 0) + 1

        dupCheck = lambda x, v: -v == nums[x] and dic[-v] > 1

        i = 0
        while i <= idx and i < len(nums)-2:
            j = i+1 if nums[i] <= 0 else idx
            while j < len(nums)-1:
                v = nums[i] + nums[j]
                if -v in dic and -v >= nums[j]:
                    if -v == nums[i] and -v == nums[j]:
                        if dic[-v] > 2:
                            sets.append([nums[i], nums[j], -v])
                    elif -v not in (nums[i], nums[j]) or dupCheck(i, v) or dupCheck(j, v):
                        sets.append([nums[i], nums[j], -v])

                j = self.next(nums, j)

            i = self.next(nums, i)

        return sets

    def next(self, nums, x):
        if nums[x] != nums[x+1]:
            x += 1
        else:
            while nums[x] == nums[x+1] and x < len(nums)-2:
                x += 1
            x += 1
        return x


s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, -4])
# [[-1, -1, 2], [-1, 0, 1]]

print s.threeSum([0, 0, 0, 0, 0, 0])
# [[0, 0, 0]]

print s.threeSum([-1, 0, 1, 2, -1, -4, 0, 0, 0])
# [[-1, -1, 2], [-1, 0, 1], [0, 0, 0]]

print s.threeSum([-1, 0])
# []

print s.threeSum([1, 2, -3, 0, -1, 1, 2, 3])
# [[-3, 0, 3], [-3, 1, 2], [-1, 0, 1]]

print s.threeSum([-1, 0, 1, 2, -1, -4, -1, 2, 0]);
# [[-4, 2, 2], [-1, -1, 2], [-1, 0, 1]]

print s.threeSum([-1, 0, 1, 2, -1, -4, -1, 2, 0, 0]);
# [[-4, 2, 2], [-1, -1, 2], [-1, 0, 1], [0, 0, 0]]


print s.threeSum([-1, -4, -4, 8]);
print s.threeSum([-4, -4, 8]);
print s.threeSum([-4, -4, -100]);


print s.threeSum([-1, 0, 1, 0])