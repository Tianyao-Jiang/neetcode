class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        self.backtrack(nums, 0, path, res)
        return res

    def backtrack(self, nums, index, path, res):        
        res.append(path.copy())

        for i in range(index, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i + 1, path, res)
            path.pop()