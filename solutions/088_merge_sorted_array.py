# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# The number of elements initialized in nums1 and nums2 are m and n respectively.

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            # return nums1 # for test
            return

        if m == 0:
            nums1[:] = nums2[:]
            # return nums1 # for test
            return

        i = j = k = 0
        while i < (m + k) and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
                k += 1
            i += 1
        
        while j < n:
            nums1[i] = nums2[j]
            i, j = i+1, j+1

        nums1[:] = nums1[:(m+n)]
        # return nums1 # for test

        # O(nlogn) with built-in function extra space
        # x = A[0:m]
        # y = B[0:n]
        # x.extend(y)
        # x.sort()
        # A[0:m+n] = x

        # O(nlogn) with built-in function
        # A[m:] = B[:n]
        # A.sort()