class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        self.backtrack(nums, path, res, 0)
        return res

    def backtrack(self, nums, path, res, index):
        
        res.append(path.copy())

        for i in range(index, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, path, res, i + 1)
            path.pop()

