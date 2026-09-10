# one maxHeap to keep track of number of each kind of letter, pops the most frequent one
# one queue to keep track of (frequency, time)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []
        for cnt in count.values():
            maxHeap.append(-1 * cnt)
        heapq.heapify(maxHeap)

        q = deque() # [-frequency, idelTime]
        t = 0
        while maxHeap or q:
            t += 1
            if maxHeap:
                val = heapq.heappop(maxHeap)
                if 1 + val < 0:
                    q.append([1 + val, t + n])
            if q and q[0][1] == t:
                heapq.heappush(maxHeap, q.popleft()[0])
        return t
        

        