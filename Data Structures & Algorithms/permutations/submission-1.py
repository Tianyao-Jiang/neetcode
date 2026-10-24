class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s = set()

        path = []
        res = []

        self.backtrack(nums, path, res, s)

        return res

    def backtrack(self, nums, path, res, s):
        if len(path) == len(nums):
            res.append(path.copy())
            return
        
        for i in range(0, len(nums)):
            if nums[i] in s:
                continue
            path.append(nums[i])
            s.add(nums[i])
            self.backtrack(nums, path, res, s)
            path.pop()
            s.remove(nums[i])