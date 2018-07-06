"""
https://leetcode.com/problems/russian-doll-envelopes/description/

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""

class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        contains = defaultdict(set)
        contained_by = defaultdict(set)
        depths = defaultdict(int)
        total = len(envelopes)
        es = set(list(range(total)))
        for i in range(total):
            for j in range(total):
                if i != j:
                    a = envelopes[i]
                    b = envelopes[j]
                    if a[0] < b[0] and a[1] < b[1]:
                        contains[j].add(i)
                        contained_by[i].add(j)
                        es.discard(j)
                    elif a[0] > b[0] and a[1] > b[1]:
                        contains[i].add(j)
                        contained_by[j].add(i)
                        es.discard(i)
        ans = 0
        while len(es) != 0:
            cur = es.pop()
            # print(envelopes[cur], depths[cur])
            if len(contained_by[cur]) == 0:
                ans = max(ans, 1+depths[cur])
            for cb in contained_by[cur]:
                depths[cb] = max(depths[cb], 1+depths[cur])
                contains[cb].discard(cur)
                if len(contains[cb]) == 0:
                    es.add(cb)

        return ans
