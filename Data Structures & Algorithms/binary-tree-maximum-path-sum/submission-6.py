# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = root.val

        def dfs(root):
            if not root:
                return 0 

            max_left = dfs(root.left)
            max_right = dfs(root.right)

            max_left = max(0, max_left)
            max_right = max(0, max_right)

            nonlocal res
            res = max(res, max_left + max_right + root.val)

            return max(max_left, max_right) + root.val

        dfs(root)

        return res
            
