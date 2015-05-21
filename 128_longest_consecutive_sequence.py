import time
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# Your algorithm should run in O(n) complexity. 

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        minNum = nums[0]
        maxNum = nums[0]
        dic = {nums[0]:nums[0]}

        for num in nums[1:]:
            if num > maxNum:
                maxNum = num
                # maxList.append(maxNum)
            elif num < minNum:
                minNum = num

            dic[num] = num

        local = 0
        longest = 1
        num = minNum
        while num <= maxNum:
            consecutive = dic.has_key(num)
            if consecutive:
                local += 1
            else:
                longest = max(longest, local)
                consecutive = True
                local = 0
            num += 1

        return max(longest, local)


s = Solution()
# print s.longestConsecutive([100])
print s.longestConsecutive([100, 100, 101]) #2
print s.longestConsecutive([102, 100, 100, 101]) #3
print s.longestConsecutive([100, 4, 200, 1, 3, 2]) #4
print s.longestConsecutive([100, 4, 1, 3, 2, 145, 146, 148, 147, 144, 300, 150]) #5

# # FAILED !!
print s.longestConsecutive([193, 100, 4, 200, 1, 3, 2, 195, 196, 198, 197, 194, 300, 150]) #6
print s.longestConsecutive([193, 100, 4, 200, 1, 3, 2, 195, 196, 198, 197, 194, 300, 150, 299, 298, 297, 296, 295, 294, 293]) #8

start_time = time.time()
print s.longestConsecutive([2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645])
print("--- %s seconds ---" % (time.time() - start_time))