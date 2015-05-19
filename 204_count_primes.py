# Count the number of prime numbers less than a non-negative number, n
# @param {integer} n
# @return {integer}

def countPrimes(n):
    
    from math import sqrt

    if n <= 2:
        return 0

    l = [True] * (n)
    l[1] = False

    for i in xrange(2, int(sqrt(n))+1):
        if l[i]:
            for j in xrange(i*i, n, i):
                l[j] = False
    l = filter(lambda x: x == True, l[1:])
    return len(l)
    
print countPrimes(0)
print countPrimes(1)
print countPrimes(2)
print countPrimes(3)
print countPrimes(4)
# print countPrimes(30)
# print countPrimes(100)     #4: 2, 3, 5, 7
print countPrimes(100)    #25:
# print countPrimes(499979)
print countPrimes(999983)


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