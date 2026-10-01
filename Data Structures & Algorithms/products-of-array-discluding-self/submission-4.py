class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [0] * len(nums)
        post = [0] * len(nums)
        res = []

        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
                continue
            pre[i] = pre[i - 1] * nums[i - 1]

        for j in range(len(nums) -1, -1, -1):
            if j == len(nums) - 1:
                post[j] = 1
                continue
            post[j] = post[j + 1] * nums[j + 1]

        for k in range(len(nums)):
            res.append(post[k] * pre[k])

        return res