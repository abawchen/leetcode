# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? 
# Find all unique quadruplets in the array which gives the sum of target.
# Note:
#     Elements in a quadruplet (a,b,c,d) must be in non-descending order.
#     The solution set must not contain duplicate quadruplets.
#     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#     A solution set is:
#     (-1,  0, 0, 1)
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        import itertools, collections

        nums.sort()
        sets = []
        answerDic = {}
        dic = collections.defaultdict(list)

        i = 0
        while i < len(nums) - 2:
            j = i+1
            while j < len(nums):
                dic[nums[i] + nums[j]].append((nums[i], nums[j]))
                j = self.next(nums, j)
            i = self.next(nums, i)
        
        for key in sorted(dic):
            print (key, dic[key])

        if target%2 == 0 and target/2 in dic:
            if len(dic[target/2]) > 1:
                answers = [sorted([a, b, c, d]) for ((a, b), (c, d)) in itertools.combinations(dic[target/2], 2)]
                for answer in answers:
                    self.putAnswer(sets, sorted([a, b, c, d]), answerDic)

            if target%4 == 0:
                if len(filter(lambda num: num == float(target)/4, nums)) >= 4:
                    sets.append([target/4]*4)
            del dic[target/2]

        for k in dic.keys():
            if target-k in dic:
                for (a, b) in dic[k]:
                    for (c, d) in dic[target-k]:
                        print (a, b, c, d)
                        self.putAnswer(sets, sorted([a, b, c, d]), answerDic)
            del dic[k]

        return sets

    def next(self, nums, x):
        while x < len(nums)-1 and nums[x] == nums[x+1]:
            x += 1
        return x+1

    def putAnswer(self, sets, answer, answerDic):
        answerStr = '#'.join(str(x) for x in answer)
        if answerStr not in answerDic:
            sets.append(answer)
        answerDic[answerStr] = True


s = Solution()

# print "sets:", s.fourSum([-1, 0, 1, 2, 2, 2, 2, -1, -4, -1, 0, -4, 4], 0)
# # [[-1, 0, 0, 1], [-1, -1, 0, 2], [-4, 0, 2, 2], [-4, -1, 1, 4], [-4, 1, 1, 2], [-4, 0, 0, 4]]
# print "=================================================================================================="


# print "sets:", s.fourSum([1, 0, -1, 0, -2, 2], 0)
# # [[-1, 0, 0, 1], [-2, -1, 1, 2], [-1, -1, 0, 2], [-2, 0, 1, 1], [-2, 0, 0, 2]]
# print "=================================================================================================="

# print "sets:", s.fourSum([0, 0, 0, 0, 0, 0], 0)
# # [[0, 0, 0, 0]]
# print "=================================================================================================="


# print "sets:", s.fourSum([1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0], 4)
# # [[0, 1, 1, 2], [1, 1, 1, 1], [0, 0, 2, 2]]
# print "=================================================================================================="


# print "sets:", s.fourSum([1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0, 6, 6, 6, 4, 4, 3, 3, 2, 3, 5, -1], 6)
# print "=================================================================================================="



# print "sets:", s.fourSum([2, 1, 0, -1], 2)
# # [[-1, 0, 1, 2]]
# print "=================================================================================================="



print "sets:", s.fourSum([1, 0, -1, 0, -2, 2], 0)
# [[-1, 0, 1, 2]]
print "=================================================================================================="

