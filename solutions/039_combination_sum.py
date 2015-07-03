# -*- coding: utf-8 -*-

# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

# Note:

#     All numbers (including target) will be positive integers.
#     Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
#     The solution set must not contain duplicate combinations.

# For example, given candidate set 2,3,6,7 and target 7,
# A solution set is:
# [7]
# [2, 2, 3] 


class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        candidates.sort()
        ans = []
        self._combinationSum(0, candidates, target, ans, [])

        return ans

    def _combinationSum(self, i, candidates, target, ans, res):
        if target == 0:
            ans.append(list(res))
            return

        for j in xrange(i, len(candidates)):
            n = candidates[j]

            if j > i and n == candidates[j - 1]:
                continue

            if n > target:
                break

            res.append(n)
            self._combinationSum(j, candidates, target-n, ans, res)
            res.pop()