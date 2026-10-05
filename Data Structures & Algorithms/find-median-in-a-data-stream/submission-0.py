class MedianFinder:

    def __init__(self):
        
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, num)
            return 

        min_of_min_heap = self.min_heap[0]

        if num >  min_of_min_heap:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        if abs(len(self.min_heap) - len(self.max_heap)) > 1:
            if len(self.min_heap) - len(self.max_heap) > 1:
                temp = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -temp)
            else:
                temp = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, temp)
        
    def findMedian(self) -> float:

        if len(self.min_heap) == len(self.max_heap):
            temp1 = self.min_heap[0]
            temp2 = -self.max_heap[0]

            return (temp1 + temp2) / 2

        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        else: 
            return -self.max_heap[0]

        
        