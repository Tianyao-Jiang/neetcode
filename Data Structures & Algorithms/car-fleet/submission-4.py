class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(key = lambda x: x[0], reverse = True)

        res = len(pair)

        slowest = float("-inf")
        for i in range(len(pair)):
            cur_pair = pair[i]
            cur_time = (target - cur_pair[0]) / cur_pair[1]
            
            
            if cur_time <= slowest:
                res -= 1
            slowest = max(slowest, cur_time)

        return res