"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""


class Solution:
    def countSmaller(self, nums):
        ans = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            val = nums[i]
            for j in range(i):
                if val < nums[j]:
                    ans[j] += 1
        return ans
        """
        for i in range(len(nums) -2, -1, -1):
            current = nums[i]
            right = nums[i + 1]
            if right < current:
                ans[i] = ans[i + 1] + 1
            else:
                for j in range(i, len(nums)):
                    if nums[j] < current:
                        ans[i] = ans[j] + 1
                        break
        return ans
        """
