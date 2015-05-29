def twoSum(nums, target):
    dic = {}
    for i, x in enumerate(nums):
        if dic.has_key(x) and dic[x] < i:
            return [dic[x]+1, i+1]
        r = target - x
        dic[r] = i

print twoSum([0,4,3,0], 0) #[1, 4]
print twoSum([3,2,4], 6) #[2, 3]
print twoSum([1,2,3,5], 7) #[2, 4]
print twoSum([2,7,11,15], 9) #[1, 2]

# Time Limit Exceeded: O(n*n)
# def twoSum(nums, target):
#     for i, x in enumerate(nums):
#         for j in xrange(i+1, len(nums)):
#             if (x + nums[j]) == target:
#                 return [i+1, j+1]
