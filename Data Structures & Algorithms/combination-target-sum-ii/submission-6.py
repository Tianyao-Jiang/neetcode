class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        self.backtrack(candidates, target, path, res, 0)

        return res

    def backtrack(self, nums, target, path, res, index):

        if target == 0:
            res.append(path.copy())
            return

        if target < 0:
            return 

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue 
            path.append(nums[i])
            self.backtrack(nums, target - nums[i], path, res, i + 1)
            path.pop()