class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):

        strNum = [str(i) for i in nums]
        strNum.sort(lambda x,y: int(y+x) - int(x+y))
        return str(int(''.join(strNum)))


        # if nums == None or len(nums) == 0:
        #     return None

        # if len(nums) == 1:
        #     return str(nums[0])

        # self.zero = True
        # nums.sort(self.cmp)

        # if self.zero:
        #     return "0"

        # return str(reduce(lambda a, b: str(a) + str(b), nums))

    def cmp(self, a, b):
        # if self.zero and (a > 0 or b > 0):
        #     self.zero = False

        # a, b =  str(a), str(b)
        # r1 = eval(a+"+"+b)
        # r2 = eval(a+"+"+b)
        # if r1 > r2:
        #     return -1

        # return 1
        if self.zero and (a > 0 or b > 0):
            self.zero = False

        a = str(a)
        b = str(b)
        for i in xrange(0, max(len(a), len(b))):
            if i < len(a) and i < len(b):
                if a[i] > b[i]:
                    return -1
                elif a[i] < b[i]:
                    return 1
            elif i >= len(a):
                if a[0] > b[i]:
                    return -1
                elif a[0] < b[i]:
                    return 1
            else:
                if b[0] > a[i]:
                    return 1
                elif b[0] < a[i]:
                    return -1

        if int(a + b) > int(b + a):
            return -1
        
        return 1

s = Solution()
# print(s.largestNumber(None))
# print(s.largestNumber([]))
print(s.largestNumber([100, 100]))
print(s.largestNumber([3, 30]))
print(s.largestNumber([30, 3]))
print(s.largestNumber([3, 30, 34, 5, 9]))
# print(s.largestNumber([12, 65, 120, 123, 456, 60, 98, 190, 8, 9, 1]))
# 99886560456190

print(s.largestNumber([1440,7548,4240,6616,733,4712,883,8,9576]))
# 9576888375487336616471242401440

print(s.largestNumber([131,13]))
# 13 131 o
# 131 13 x

print(s.largestNumber([135,13]))
# 13513 o
# 13135 x

print(s.largestNumber([132,13]))
# 13213 o
# 13132

print(s.largestNumber([8, 883]))
print(s.largestNumber([883, 8]))
print(s.largestNumber([1]))
print(s.largestNumber([0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(s.largestNumber([1, 0, 0]))
# print(type(s.largestNumber([1])))

print(s.largestNumber([824,938,1399,5607,6973,5703,9609,4398,8247]))
# 9609938824824769735703560743981399


print(s.largestNumber([8308,830]))
#8308830 o
#8308308 x
# print(s.largestNumber([830,8308]))


print(s.largestNumber([9051,5526,2264,5041,1630,5906,6787,8382,4662,4532,6804,4710,4542,2116,7219,8701,8308,957,8775,4822,396,8995,8597,2304,8902,830,8591,5828,9642,7100,3976,5565,5490,1613,5731,8052,8985,2623,6325,3723,5224,8274,4787,6310,3393,78,3288,7584,7440,5752,351,4555,7265,9959,3866,9854,2709,5817,7272,43,1014,7527,3946,4289,1272,5213,710,1603,2436,8823,5228,2581,771,3700,2109,5638,3402,3910,871,5441,6861,9556,1089,4088,2788,9632,6822,6145,5137,236,683,2869,9525,8161,8374,2439,6028,7813,6406,7519]))
