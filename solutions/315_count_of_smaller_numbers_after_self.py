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

    def searchSmaller(self, nums, num):
        if len(nums) == 0 or num <= nums[0]:
            return 0
        if num > nums[-1]:
            return len(nums)

        start, end = 0, len(nums)
        while True:
            middle = int((start + end) / 2)
            left = middle - 1
            if num <= nums[middle]:
                if num > nums[left]:
                    return middle
                end = middle
            else:
                start = middle

    def countSmaller(self, nums):
        ans = [0] * len(nums)
        sort = []

        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            ans[i] = self.searchSmaller(sort, num)
            sort.insert(ans[i], num)
        return ans

