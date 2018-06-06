class Solution:

    ugly_nums = [1]
    ugly_status = [(1, 0)]
    ugly_primes = [2, 3, 5]

    def nthUglyNumber(self, n):
        import sys
        while n > len(Solution.ugly_nums):
            mi = -1
            pi = 3
            minimum = sys.maxint
            print('*' * 10)
            for i, (u, p) in enumerate(Solution.ugly_status):
                print(minimum, i, (u, p))
                if p > pi:
                    break

                m = u * Solution.ugly_primes[p]
                if m < minimum:
                    print('here:', m)
                    minimum = m
                    mi = i
                    pi = p
                elif m == minimum:
                    if p == 2:
                        Solution.ugly_status.pop(i)
                    else:
                        Solution.ugly_status[i] = (m, p + 1)
                    break
                elif m > minimum:
                    break

            (u, p) = Solution.ugly_status[mi]
            if p == 2:
                Solution.ugly_status.pop(mi)
            else:
                Solution.ugly_status[mi] = (u, p + 1)
            # print((m, 0))
            print(Solution.ugly_status)
            print(m)
            print('&' * 10)
            Solution.ugly_nums += [minimum]
            Solution.ugly_status += [(minimum, 0)]

        print(Solution.ugly_nums)
        return Solution.ugly_nums[n-1]

    '''
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
    '''
