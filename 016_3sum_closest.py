# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

import time

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        
        dic = {}
        nums.sort()
        result = sum(nums[:3])
        closest = abs(target - result)
        for i in xrange(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                gap = abs(target - temp)

                if gap == 0:
                    return target

                if gap < closest:
                    closest = gap
                    result = temp

                if temp < target:
                    j += 1
                else:
                    k -= 1

        return result

s = Solution()

print s.threeSumClosest([-1, 0, 1, 2, -1, -4], 0) # 0
print s.threeSumClosest([-1, 2, 1, -4], 2) # 2
print s.threeSumClosest([-1, 2, 1, -4], 1) # 2
print s.threeSumClosest([0, 0, 0, 0, 0, 0], 8) # 0
print s.threeSumClosest([-1, 0, 0, -1, 0, -1, 0], 8) # 0
print s.threeSumClosest([-1, 0, 1, 2, -1, -4, 0, 0, 0], 0) # 0
print s.threeSumClosest([1, 2, -3, 0, -1, 1, 2, 3], 0) # 0
print s.threeSumClosest([-1, 0, 1, 2, -1, -4, -1, 2, 0], 0) # 0
print s.threeSumClosest([-1, 0, 1, 2, -1, -4, -1, 2, 0, 0], 0) # 0
print s.threeSumClosest([-1, -4, -4, 8], 0) # 0
print s.threeSumClosest([-4, -4, -100], 0) # -108
print s.threeSumClosest([-4, -4, -100, 5, 10, 20, 30, 40, 50], 0) # 2 (-4, -4, 10)
print s.threeSumClosest([-4, -3, -100, 5, 10, 10, 10, 20, 30, 40, 50], 8) # 11 (-4, 5, 10)
print s.threeSumClosest([-1, 0, 1, 0], 0) # 0
print s.threeSumClosest([-1, -5, -3, -4, 2, -2], 0) # -1

l = [35,28,94,27,0,1,-89,-20,60,-51,35,67,-94,-78,-67,-60,52,40,-4,99,-26,-26,-77,61,-28,9,66,-40,-2,45,59,-37,59,-90,76,100,20,83,37,-65,20,-95,16,-77,-18,53,93,-88,-33,46,-30,-77,-36,79,34,-3,-84,72,-66,-84,-36,94,-26,11,-23,35,1,36,-70,76,-24,91,-9,-73,43,-92,93,39,99,44,73,7,90,-77,-92,-62,-63,90,-81,80,18,68,-89,95,-22,74,-50,-34,58,-64,61,-30,44,-28,48,13,-45,-75,19,86,40,68,74,-62,44,-12,-18,61,95,53,-63,6,46,-74,82,-39,-52,-45,-41,55,99,22,41,-45,-37,-9,-62,-41,28,5,-40,-99,-83,49,15,75,-36,97,79,-45,-4,-82,-2,6,3,-7,-21,68,81,94,-87,76,64,-32,80,-91,65,-84,-61,-64,68,-73,8,-25,23,51,53,-30,65,92,73,-96,20,70,0,10,-37,90,90,0]
start_time = time.time()
print s.threeSumClosest(l, -9)
print("--- %s seconds ---" % (time.time() - start_time))

