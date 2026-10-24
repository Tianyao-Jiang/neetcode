class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []
        path = []

        self.backtrack(nums, path, res, 0)
        return res

    def backtrack(self, nums, path, res, index):

        res.append(path.copy())

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            self.backtrack(nums, path, res, i + 1)
            path.pop()