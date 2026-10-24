# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        self.dfs(root, root.val)

        return self.res

    def dfs(self, root, curMax):
        if not root:
            return 

        if root.val >= curMax:
            self.res += 1
        
        curMax = max(curMax, root.val)

        self.dfs(root.left, curMax)
        self.dfs(root.right, curMax)
        