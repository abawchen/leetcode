class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        if nums1 == None:
            nums1 = []
        if nums2 == None:
            nums2 = []

        i = 0
        j = 0
        nums = []
        l1 = len(nums1)
        l2 = len(nums2)
        while i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        nums.extend(nums1[i:])
        nums.extend(nums2[j:])
        if nums:
            mid = len(nums)/2
            return float(nums[mid]) if len(nums) % 2 != 0 else (nums[mid]+nums[mid-1])/2.0


s = Solution()
# print(s.findMedianSortedArrays([], [1, 2]))
print(s.findMedianSortedArrays([], []))
print(s.findMedianSortedArrays([1, 3, 3], None))
print(s.findMedianSortedArrays([], [1, 2, 3]))
print(s.findMedianSortedArrays([1, 2, 3], []))
# print(s.findMedianSortedArrays([], range(130, 136)))

print(s.findMedianSortedArrays([1, 3], [2, 4, 6, 8]))

# a = [60000]
# b = [50000]
# c = [30000]*2
# d = [15000]*22
# e = [5000]*24
# l = e + d + c + b + a
# print l
# print(s.findMedianSortedArrays([], l))