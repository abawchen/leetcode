# Count the number of prime numbers less than a non-negative number, n
# @param {integer} n
# @return {integer}

def countPrimes(n):

    from math import sqrt

    if n <= 2:
        return 0

    l = [True] * (n)
    l[1] = False

    for i in range(2, int(sqrt(n))+1):
        if l[i]:
            for j in range(i*i, n, i):
                l[j] = False
    # print(l)
    l = list(filter(lambda x: x == True, l[1:]))
    # print(l)
    return len(list(l))

# print(0, countPrimes(0))
# print(1, countPrimes(1))
# print(2, countPrimes(2))
print(3, countPrimes(3))
print(4, countPrimes(4))
print(14, countPrimes(14))
# print(100, countPrimes(100))
# print(999983, countPrimes(999983))
from math import pow
big = int(pow(2, 31))
print(countPrimes(big))

# TIME LIMIT EXCEEDED @ 999983
# def countPrimes(n):
#     if n <= 3:
#         return n-2
#     primes = [2]
#     l = xrange(3, n)
#     l = filter(lambda x: x % 2 != 0, l)
#     isPrime = True
#     while isPrime:
#         t = l[0]
#         if t*t <= n and l[0] % primes[-1] != 0:
#             l = filter(lambda x: x % t != 0, l)
#             primes.extend([t])
#         else:
#             isPrime = False
#     primes.extend(l)
#     # print primes
#     return len(primes)
# print countPrimes(999983)


# TIME LIMIT EXCEEDED @ 499979
# def countPrimes(n):
#     if n <= 2:
#         return 0
#     primes = [2]
#     a = xrange(3, n)
#     for i in xrange(3, n):
#         isPrime = True
#         for p in primes:
#             if i % p == 0:
#                 isPrime = False
#                 break;
#         if isPrime:
#             primes.extend([i])
#     # print primes
#     return len(primes)
# print countPrimes(499979)


# def countPrimes(n):
#     if n <= 2:
#         return 0

#     primes = [2]
#     l = xrange(3, n)
#     l = filter(lambda x: x % 2 != 0, l)

#     isPrime = True
#     while isPrime:
#         t = l[0]
#         if t*t <= n and l[0] % primes[-1] != 0:
#             p = l[0]
#             l = filter(lambda x: x % p != 0, l)
#             primes.extend([p])
#         else:
#             isPrime = False

#     primes.extend(l)
#     return len(primes)
    
# print countPrimes(499979)
