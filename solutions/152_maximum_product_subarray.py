# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6. 


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):

        fn = 0 if nums[0] >= 0 else 1
        val = 1 if nums[0] == 0 else nums[0]
        ans = nums[0]

        for n in nums[1:]:
            if n == 0:
                fn, val, ans = 0, 1, max(ans, 0)
                continue

            if n < 0 and fn == 0:
                fn, val = 1, val*n
                continue

            fn, val = fn*n, val*n
            ans = max(ans, val, fn)

        return ans



