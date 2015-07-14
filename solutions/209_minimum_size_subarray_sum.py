class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):

        val = start = 0
        minLength = len(nums) + 1

        for i in xrange(len(nums)):
            
            if nums[i] >= s:
                return 1

            val += nums[i]
            
            if val >= s:

                while val - nums[start] >= s:
                    val -= nums[start]
                    start += 1
                minLength = min(minLength, i - start + 1)

                if i < len(nums) - 1:
                    n = nums[i+1]
                    while n > 0:
                        val -= nums[start]
                        n -= nums[start]
                        start += 1

        return minLength if minLength != len(nums) + 1 else 0