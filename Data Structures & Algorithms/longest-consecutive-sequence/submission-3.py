class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set()
        res = 0
        for num in nums:
            s.add(num)

        for i in range(len(nums)):
            cur = nums[i]
            if (cur - 1) in s:
                continue
            l = nums[i]
            temp = 0
            while l in s:
                l += 1
                temp += 1
                
            res = max(res, temp)
        return res
