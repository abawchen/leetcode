class Solution:

    ugly_nums = [1, 2, 3, 4, 5]
    def nthUglyNumber(self, n):
        if n < 5:
            return Solution.ugly_nums[n-1]
        
        while n > len(Solution.ugly_nums):
            c = Solution.ugly_nums[-1]            
            found = False
            while not found:
                c += 1
                for u in [2, 3, 5]:
                    if c % u == 0 and int(c / u) in Solution.ugly_nums:
                        Solution.ugly_nums += [c]
                        found = True
                        break

        return Solution.ugly_nums[n-1]
