import heapq
class MedianFinder:

    def __init__(self):
        self.a = []
        self.b = []
        self.median = None
        
    def addNum(self, num: int) -> None:
        if self.median is not None:
            x, y = self.median, num
            if x > y:
                x, y = y, x
            heapq.heappush(self.a, ~x)
            heapq.heappush(self.b, y)
            self.median = None
        else:
            if not self.a or num <= ~self.a[0]:
                heapq.heappush(self.a, ~num)
                self.median = ~heapq.heappop(self.a)
            else:
                heapq.heappush(self.b, num)
                self.median = heapq.heappop(self.b)
            
    def findMedian(self) -> float:
        if self.median is not None:
            return self.median
        
        return (~self.a[0] + self.b[0]) / 2