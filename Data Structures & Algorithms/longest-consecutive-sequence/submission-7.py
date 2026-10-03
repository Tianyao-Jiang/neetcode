class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        res = 0
        for num in s:
            if (num - 1) in s:
                continue
            l = num
            temp = 0
            while l in s:
                l += 1
                temp += 1
                
            res = max(res, temp)
        return res
