class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []

        for key, value in count.items():
            heapq.heappush(heap, (-value, key))
        
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res