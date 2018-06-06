class Solution:

    ugly_nums = [1]
    ugly_set = {1}
    ugly_status = [(1, 0)]
    ugly_primes = [2, 3, 5]

    def nthUglyNumber(self, n):
        while n > len(Solution.ugly_nums):
            mi = -1
            pi = 3
            minimum = float('inf')
            for i, (u, p) in enumerate(Solution.ugly_status):
                if p > pi:
                    break

                m = u * Solution.ugly_primes[p]
                while m in Solution.ugly_set:
                    if p == 2:
                        Solution.ugly_status.pop(i)
                        break
                    p += 1
                    Solution.ugly_status[i] = (u, p)
                    m = u * Solution.ugly_primes[p]
                if m < minimum:
                    minimum = m
                    mi = i
                    pi = p
                elif m == minimum:
                    if p == 2:
                        Solution.ugly_status.pop(i)
                    else:
                        Solution.ugly_status[i] = (u, p + 1)
                    # break <-- will failed if early break, not check the reason yet
            (u, p) = Solution.ugly_status[mi]
            if p == 2:
                Solution.ugly_status.pop(mi)
            else:
                Solution.ugly_status[mi] = (u, p + 1)
            Solution.ugly_nums += [minimum]
            Solution.ugly_set.add(minimum)
            Solution.ugly_status += [(minimum, 0)]

        return Solution.ugly_nums[n-1]
