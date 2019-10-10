# 56
# https://leetcode.com/problems/merge-intervals/
# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

class Solution:
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        key = lambda x: x[0]
        intervals = sorted(intervals, key=key)
        curMin = None
        curMax = None
        returnIntervals = []
        for tup in intervals:
            if curMin is None:
                curMin = tup[0]
                curMax = tup[1]
            elif curMax < tup[0]:
                returnIntervals.append([curMin, curMax])
                curMax = tup[1]
                curMin = tup[0]
            else:
                curMax = max(curMax, tup[1])
        returnIntervals.append([curMin, curMax])
        return returnIntervals