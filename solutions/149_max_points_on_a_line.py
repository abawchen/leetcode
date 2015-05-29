# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        if points == None or len(points) == 0:
            return 0

        dic = {}
        fdic = {}
        pdic = {}
        answer = 1
        isOnLine = (lambda p, (z, a, b): abs((z * p.y) - (a * p.x + b)) < 0.0000001)

        cp = points[:]
        for p in cp:
            if dic.has_key((p.x, p.y)):
                dic[(p.x, p.y)] += 1
                points.remove(p)
                answer = max(answer, dic[(p.x, p.y)])
            else:    
                dic[(p.x, p.y)] = 1

        count = len(points)
        for i in xrange(0, count):
            p1 = points[i]
            for j in xrange(i + 1, count):
                p2 = points[j]
                key = self.buildLine(p1, p2)
                # print i, j, key
                if fdic.has_key(key):
                    # print key
                    if pdic[key] == i:
                        fdic[key] += dic[(p2.x, p2.y)]
                else:
                    pdic[key] = i
                    fdic[key] = dic[(p1.x, p1.y)] + dic[(p2.x, p2.y)]

                answer = max(answer, fdic[key])


        # for i in xrange(0, count):
        #     p1 = points[i]
        #     for j in xrange(i + 1, count):
        #         p2 = points[j]
        #         fdic[self.buildLine(p1, p2)] = True

        # for key in fdic:
        #     r = 0
        #     for p in points:
        #         r += 1 if isOnLine(p, key) else 0
        #     answer = max(answer, r)

        return answer

    def buildLine(self, p1, p2):
        if p1.x == p2.x:
            return (0, 1, -p1.x)
        else:
            a = (float(p2.y) - p1.y)/(p2.x - p1.x)
            b = p1.y - a * p1.x
            return (1.0, a, b)


pts = [
    
    # Point(0, 0),
    # Point(0, 0),

    # Point(3,10),
    # Point(0,2),
    # Point(0,2),
    # Point(3,10)

    # Point(1,1),
    # Point(1,1),
    # Point(2,3)

    # Point(0,0),
    # Point(-1,-1),
    # Point(2,2)


    # Point(-1, -1),
    # Point(2, 2),
    # Point(0, 2),
    # Point(1, 0),
    # Point(1, 1),
    # Point(1, 2),
    # Point(1, 3),
    # Point(1, 4)

    # Point(3, 1),
    # Point(12, 3),
    # Point(3, 1),
    # Point(-6, -1)

    # Point(-4, -4),
    # Point(-8, -582),
    # Point(-3, 3),
    # Point(-9, -651),
    # Point(9, 591),


    Point(0,9),
    Point(138,429),
    Point(115,359),
    Point(115,359),
    Point(-30,-102),
    Point(230,709),
    Point(-150,-686),
    Point(-135,-613),
    Point(-60,-248),
    Point(-161,-481),
    Point(207,639),
    Point(23,79),
    Point(-230,-691),
    Point(-115,-341),
    Point(92,289),
    Point(60,336),
    Point(-105,-467),
    Point(135,701),
    Point(-90,-394),
    Point(-184,-551),
    Point(150,774)
]

s = Solution()
print(s.maxPoints(pts))

# y = ax + b
# 0 = 2a + b #(2, 0)
# 1 = 3a + b #(3, 1)
# (3-2)a = (1-0)
# a = delta_y/delta_x
# b = y - ax

# 0 = 2a + b #(2, 0)
# 1 = 2a + b #(2, 1)
# (2-2)a = (1-0)
# 0y = x - 2
# (2, 5)

# 1y = 0x + b

# key = (z, a, b) # z = 1 at most cases


# Failed, no consideration on slope ... Orz
# class Solution:
#     # @param {PointPoint(]} points
#     # @return {integer}
#     def maxPoints(self, points):
#         if points == None or len(points) == 0:
#             return 0

#         dic = {}
#         hdic = {}
#         vdic = {}
#         rudic = {}
#         ludic = {}
        
#         for p in points:
#             v = dic.get((p.x, p.y), 0)
#             dic[(p.x, p.y)] = v + 1

#         answer = 0
#         for (x, y) in dic:
            
#             # horizontal
#             d = dic[(x, y)]
#             if not hdic.has_key((x, y)):
#                 hdic[(x, y)] = True

#                 # go left
#                 a, b = x, y
#                 while dic.has_key((a - 1, b)):
#                     a -= 1
#                     hdic[(a, b)] = True
#                     d += dic[(a, b)]
                
#                 # go right
#                 a, b = x, y
#                 while dic.has_key((a + 1, b)):
#                     a += 1
#                     hdic[(a, b)] = True
#                     d += dic[(a, b)]
#             answer = max(answer, d)

#             # vertical
#             d = dic[(x, y)]
#             if not vdic.has_key((x, y)):
#                 vdic[(x, y)] = True

#                 # go up
#                 a, b = x, y
#                 while dic.has_key((a, b - 1)):
#                     b -= 1
#                     vdic[(a, b)] = True
#                     d += dic[(a, b)]
                    
#                 # go down
#                 a, b = x, y
#                 while dic.has_key((a, b + 1)):
#                     b += 1
#                     vdic[(a, b)] = True
#                     d += dic[(a, b)]
#             answer = max(answer, d)

#             # ru
#             d = dic[(x, y)]
#             if not rudic.has_key((x, y)):
#                 rudic[(x, y)] = True

#                 # go ru
#                 a, b = x, y
#                 while dic.has_key((a + 1, b + 1)):
#                     a += 1
#                     b += 1
#                     rudic[(a, b)] = True
#                     d += dic[(a, b)]
                    
#                 # go ld
#                 a, b = x, y
#                 while dic.has_key((a - 1, b - 1)):
#                     a -= 1
#                     b -= 1
#                     rudic[(a, b)] = True
#                     d += dic[(a, b)]
#             answer = max(answer, d)

#             # lu
#             d = dic[(x, y)]
#             if not ludic.has_key((x, y)):
#                 ludic[(x, y)] = True

#                 # go lu
#                 a, b = x, y
#                 while dic.has_key((a - 1, b + 1)):
#                     a -= 1
#                     b += 1
#                     ludic[(a, b)] = True
#                     d += dic[(a, b)]
                    
#                 # go rd
#                 a, b = x, y
#                 while dic.has_key((a + 1, b - 1)):
#                     a += 1
#                     b -= 1
#                     ludic[(a, b)] = True
#                     d += dic[(a, b)]
#             answer = max(answer, d)

#         return answer


        # for i in xrange(0, count - 1):
        #     p1 = points[0]
        #     for j in xrange(i + 1, count):
        #         p2 = points[j]
        #         key = self.buildLine(p1, p2)
        #         fdic[key] = True                
        #         # if fdic.has_key(key):
        #         #     continue

        #         # fdic[key] = True
        #         # d = 2
        #         # for k in xrange(j + 1, count):
        #         #     if isOnLine(points[k], key):
        #         #         d += 1

        #         # answer = max(answer, d)

