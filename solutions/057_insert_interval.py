# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]. 

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        newIntervals = []
        for i, interval in enumerate(intervals):
            if newInterval.end < interval.start:
                newIntervals += [newInterval] + intervals[i:]
                break
            elif interval.start <= newInterval.start and interval.end >= newInterval.end:
                newIntervals += intervals[i:]
                break
            elif newInterval.start <= interval.start and newInterval.end >= interval.end:
                continue
            elif newInterval.start > interval.end:
                newIntervals += [interval]
            else:
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)

        if not newIntervals or newInterval.start > newIntervals[-1].end:
            newIntervals += [newInterval]

        return newIntervals

