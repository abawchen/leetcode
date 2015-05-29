class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        if not nums:
            return

        length = len(nums)
        k = k % length
        if k:
            nums[:] = nums[-k:] + nums[:length-k]
        # dup = nums[:]*2
        # nums = dup[(length-k):2*length-k]
        print nums
        # , ((length-k), 2*length-k), len(nums)
        # print (length-k), (k+1)+length


s = Solution()
s.rotate(None, 0)
s.rotate([], 0)
s.rotate([1], 0)
s.rotate([1], 2)
s.rotate([1, 2, 3, 4, 5, 6, 7], 0)
s.rotate([1, 2, 3, 4, 5, 6, 7], 1)
s.rotate([1, 2, 3, 4, 5, 6, 7], 2)
s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
s.rotate([1, 2, 3, 4, 5, 6, 7], 4)
s.rotate([1, 2, 3, 4, 5, 6, 7], 5)
s.rotate([1, 2, 3, 4, 5, 6, 7], 6)
s.rotate([1, 2, 3, 4, 5, 6, 7], 7)
s.rotate([1, 2, 3, 4, 5, 6, 7], 8)
s.rotate([1, 2], 0)
s.rotate([1, 2], 1)
s.rotate([1, 2], 2)
s.rotate([1, 2], 3)