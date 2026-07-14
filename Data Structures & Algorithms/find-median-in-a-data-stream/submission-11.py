class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if not self.minHeap and not self.maxHeap:
            heapq.heappush(self.minHeap, num)
            print("maxHeap:", self.maxHeap,"minHeap:", self.minHeap)
            print(1)
            return
        elif not self.minHeap:
            mid = -1 * self.maxHeap[0]
            if mid > num:
                heapq.heappop(self.maxHeap)
                heapq.heappush(self.maxHeap, -1 * num)
                heapq.heappush(self.minHeap, mid)
            else:
                heapq.heappush(self.minHeap, num)
            print("maxHeap:", self.maxHeap,"minHeap:", self.minHeap)
            print(2)
            return
        elif not self.maxHeap:
            mid = self.minHeap[0]
            if mid < num:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, num)
                heapq.heappush(self.maxHeap, -1 * mid)
            else:
                heapq.heappush(self.maxHeap, -1 * num)
            print("maxHeap:", self.maxHeap,"minHeap:", self.minHeap)
            print(3)
            return
        else:
            if len(self.minHeap) - len(self.maxHeap) >= 1:
                mid = self.minHeap[0]
                if mid < num:
                    heapq.heappop(self.minHeap)
                    heapq.heappush(self.minHeap, num)
                    heapq.heappush(self.maxHeap, -1 * mid)
                else:
                    heapq.heappush(self.maxHeap, -1 * num)
                print(4)
            elif len(self.maxHeap) - len(self.minHeap) >= 1:
                mid = -1 * self.maxHeap[0]
                if mid > num:
                    heapq.heappop(self.maxHeap)
                    heapq.heappush(self.maxHeap, -1 * num)
                    heapq.heappush(self.minHeap, mid)
                else:
                    heapq.heappush(self.minHeap, num)
                print(5)
            else:
                top = -1 * self.maxHeap[0]
                bottom = self.minHeap[0]
                if num <= top:
                    heapq.heappush(self.maxHeap, -1 * num)
                else:
                    heapq.heappush(self.minHeap, num)
                print(6)
            print("maxHeap:", self.maxHeap,"minHeap:", self.minHeap)
        
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2
        
        