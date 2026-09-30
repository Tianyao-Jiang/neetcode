class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []

        for key, value in count.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = [0] * k
        for i in range(k):
            res[i] = heapq.heappop(heap)[1]

        return res