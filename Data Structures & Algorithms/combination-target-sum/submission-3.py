class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        self.backtrack(nums, target, path, res, 0)

        return res
    def backtrack(self, nums, target, path, res, index):

        if target == 0:
            res.append(path.copy())
            return

        if target < 0:
            return

        for i in range(index, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, target - nums[i], path, res, i)
            path.pop() 