# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!


class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        if not height:
            return 0

        # find the first incline
        i, pre = 0, height[0]
        for i in xrange(1, len(height)):
            if height[i] < pre:
                break
            pre = height[i]

        # no trap formed
        if i+1 == len(height):
            return 0

        pos, maximum = 0, height[i-1]
        boundaries = [(i-1, height[i-1])]
        for j in range(i, len(height)):
            if height[j] == pre:
                continue

            if height[j] > pre:
                if height[j] >= maximum:
                    x = boundaries[pos]
                    boundaries = boundaries[:pos] + [(x[0], x[1], 'x'), (j, height[j], 'x')]
                    if height[j] > maximum:
                        pos, maximum = len(boundaries)-1, height[j]
                else:
                    for b in xrange(len(boundaries)-1, -1, -1):
                        if boundaries[b][1] > height[j]:
                            x = boundaries[b]
                            boundaries = boundaries[:b] + [(x[0], x[1], 'x')]+ [(j, height[j], 'x')]
                            break
            else:
                boundaries.append((j, height[j]))

            pre = height[j]


        ans = 0
        for b in xrange(len(boundaries)-1):
            s, e = boundaries[b], boundaries[b+1]
            if 'x' in s and 'x' in e:
                h = min(s[1], e[1])
                for i in xrange(s[0]+1, e[0]):
                    ans += max(0, h-height[i])

        return ans