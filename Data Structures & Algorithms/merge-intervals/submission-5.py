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
        