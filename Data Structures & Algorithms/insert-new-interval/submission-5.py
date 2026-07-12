class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[List[int]]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # Case 1:
            # The new interval ends before the current interval starts.
            # Since intervals are sorted, we can insert newInterval here
            # and append all remaining intervals.
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            # Case 2:
            # The current interval ends before the new interval starts.
            # There is no overlap, so keep the current interval.
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # Case 3:
            # The intervals overlap. Merge them by expanding newInterval
            # to cover both ranges. Continue checking later intervals.
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]

        # If we never inserted newInterval, it belongs at the end.
        res.append(newInterval)
        return res