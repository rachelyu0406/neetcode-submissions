"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# have sorted start and end times array
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0 # count is current number meeting rooms
        # res is max number of meeting rooms ever needed
        s, e = 0, 0 # index of start and end array pointer
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
                res = max(res, count)
            else: # end ends first or ends at the same time as next start
                e += 1
                count -= 1
        return res