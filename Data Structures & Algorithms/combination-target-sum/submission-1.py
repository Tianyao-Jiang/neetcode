class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        self.backtrack(nums, 0, target, res, path)

        return res

    def backtrack(self, nums, index, target, res, path):
        if target == 0:
            res.append(path.copy())
            return 
            
        if target < 0:
            return

        for i in range(index, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i, target - nums[i], res, path)
            path.pop()
        

