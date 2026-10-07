# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(root):
            if not root:
                return 0
            nonlocal res
            leftheight = dfs(root.left) 
            rightheight = dfs(root.right)
            res = max(res, leftheight + rightheight)

            return 1 + max(leftheight, rightheight)
        dfs(root)
        return res