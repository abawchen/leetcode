# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18]. 


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if not intervals:
            return intervals

        from operator import attrgetter

        intervals.sort(key=attrgetter('start', 'end'))
        newIntervals = []
        pre = intervals[0]
        for i, interval in enumerate(intervals[1:]):
            if pre.end < interval.start:
                newIntervals += [pre]
                pre = interval
            elif pre.start > interval.end:
                newIntervals += [interval]
            else:
                pre.start = min(pre.start, interval.start)
                pre.end = max(pre.end, interval.end)

        if not newIntervals or pre.start > newIntervals[-1].end:
            newIntervals += [pre]

        return newIntervals