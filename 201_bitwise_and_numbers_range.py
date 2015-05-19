# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
# For example, given the range [5, 7], you should return 4. 

from math import log


def rangeBitwiseAnd(m, n):
    from math import log

    if m == n:
        return m

    result = 0
    u = int(log(n, 2))
    number = n - m + 1

    for i in xrange(1, u+1):
        base = 2 ** i
        if number <= base:
            start = m % (base*2)
            if start >= base and (start + number) <= (base*2):
                result += base  

    return result

# Wrong Anwser by bitwise EOR 
# def rangeBitwiseAnd(m, n):
#     from math import log

#     if m == n:
#         return m

#     result = 0
#     d = n - m + 1
#     x = int(log(n, 2)) + 1
#     for i in xrange(2, x+1):
#         y = (2 ** i)
#         step = d % y
#         if step != 0:
#             # print "step =====> ", step
#             oneStartPointer = 2**(i-1)
#             # a = ([0]*oneStartPointer + [1]*oneStartPointer) #* 2
#             # print a
#             startNumber = n - step + 1
#             startPointer = startNumber % y
#             oneCount = 0
#             if startPointer < oneStartPointer:
#                 step = step - (oneStartPointer - startPointer)
#                 if step > y:
#                     loopbackStep = step - y
#                     if loopbackStep > y:
#                         oneCount += loopbackStep - y
#                 elif step > 0:
#                     oneCount = min(step, oneStartPointer)
#             else:
#                 if (startPointer + step) > oneStartPointer * 2:
#                     # pass
#                     loopbackStep = (startPointer + step) - (oneStartPointer * 2)
#                     oneCount = oneStartPointer - (startPointer - oneStartPointer)
#                     if loopbackStep > oneStartPointer:
#                         oneCount += loopbackStep - oneStartPointer
#                 else:
#                     result += oneStartPointer
#                     oneCount = min(step, oneStartPointer)
#             # print "startNumber:", startNumber
#             # print "startPointer:", startPointer
#             # print "oneCount:", oneCount

#             result += (oneCount % 2) * oneStartPointer

#     if (int(d/2)%2 == 1 and m%2 == 0) or (int(d/2)%2 == 0 and n%2 == 1):        
#         result += 1


#     return result

# Time Limit Exceeded @ Last executed input: 20000, 2147483647
# def rangeBitwiseAnd(m, n):
#     from math import log

#     if m == n:
#         return 0
    
#     result = 0
#     d = n - m + 1
#     x = int(log(n, 2)) + 1
#     for i in xrange(2, x+1):
#         y = (2 ** i)
#         mod = d % y
#         if mod != 0:
#             k = 0
#             r = range(n-mod+1, n+1)
#             for j in r:
#                 if len(bin(j)[2:]) >= i:
#                     k += int(bin(j)[2:][-i])
#             result += ((k % 2) * 2 ** (i-1))

#     if (int(d/2)%2 == 1 and m%2 == 0) or (int(d/2)%2 == 0 and n%2 == 1):        
#         result += 1

#     return result


# Time Limit Exceeded @ Last executed input: 24, 57
# def rangeBitwiseAnd(m, n):
#     from math import log
#     if m == n:
#         return 0
#     x = int(log(n, 2)) + 1
#     l = [0] * x
#     for i in xrange(m, n+1):
#         bits = bin(i)[2:]
#         length = len(bits)
#         for j in xrange(0, length):
#             l[length-1-j] += int(bits[j])
#     l = [ (x % 2) * (2 ** idx) for idx, x in enumerate(l) ]
#     return reduce(lambda x,y: x+y, l)

# print rangeBitwiseAnd(16, 44)

# print rangeBitwiseAnd(0, 1)
# print rangeBitwiseAnd(2, 3)
# print rangeBitwiseAnd(2, 6)
# print rangeBitwiseAnd(5, 7)
# print rangeBitwiseAnd(4, 8)
# print rangeBitwiseAnd(8, 15)
# print rangeBitwiseAnd(16, 31)
print rangeBitwiseAnd(8+16, 15+17)
# print rangeBitwiseAnd(0, 4)
# print rangeBitwiseAnd(100, 120)
# print rangeBitwiseAnd(99, 123)
# print rangeBitwiseAnd(99, 122)
# print rangeBitwiseAnd(9, 32)
# print rangeBitwiseAnd(20000, 2147483647)
