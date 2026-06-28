# Sort intervals by start time.
# Go through each interval and compare it with the last interval in res.
# If they overlap, merge them by updating the end time.
# If they do not overlap, add the current interval as a new interval.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            if res:
                if res[-1][1] >= intervals[i][0]:
                    if res[-1][1] <= intervals[i][1]:
                        res[-1][1] = max(res[-1][1], intervals[i][1])
                else:
                    res.append(intervals[i])
            else:
                res.append(intervals[i])
        return res