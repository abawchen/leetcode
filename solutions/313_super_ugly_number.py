class Solution:

    def nthSuperUglyNumber(self, n, primes):
        nums = [1]
        nums_set = set(nums)
        status = [(p, p, 1) for p in primes]
        candidate_set = set(primes)
        while n > len(nums):
            next, prime, index = status.pop(0)
            nums_set.add(next)
            nums += [next]

            if n == len(nums):
                break

            while index < len(nums):
                val = prime * nums[index]
                index += 1
                if val not in candidate_set:
                    if len(status) == 0 or val > status[-1][0]:
                        i = len(status)
                    else:
                        for i, (c, _, _) in enumerate(status):
                            if val < c:
                                break
                    status.insert(i, (val, prime, index))
                    candidate_set.add(val)
                    break
        return nums[n-1]

    '''
    def nthSuperUglyNumber(self, n, primes):
        ugly_nums = [1]
        ugly_set = {1}
        ugly_status = [(1, 0)]
        while n > len(ugly_nums):
            mi = -1
            pi = 3
            minimum = float('inf')
            for i, (u, p) in enumerate(ugly_status):

                m = u * primes[p]
                while m in ugly_set:
                    if p == 2:
                        ugly_status.pop(i)
                        break
                    p += 1
                    ugly_status[i] = (u, p)
                    m = u * primes[p]
                if m < minimum:
                    minimum = m
                    mi = i
                    pi = p
                elif m == minimum:
                    if p == len(primes) - 1:
                        ugly_status.pop(i)
                    else:
                        ugly_status[i] = (u, p + 1)
            (u, p) = ugly_status[mi]
            if p == len(primes) - 1:
                ugly_status.pop(mi)
            else:
                ugly_status[mi] = (u, p + 1)
            ugly_nums += [minimum]
            ugly_set.add(minimum)
            ugly_status += [(minimum, 0)]

        return ugly_nums[n-1]
    '''
