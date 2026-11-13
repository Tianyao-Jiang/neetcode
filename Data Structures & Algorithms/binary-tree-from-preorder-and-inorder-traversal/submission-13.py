class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = {val: i for i, val in enumerate(inorder)}

        def dfs(index, inorder_l, inorder_r):
            if inorder_l > inorder_r:
                return None

            cur = preorder[index]
            cur_pos_in_inorder = m[cur]
            left_size = cur_pos_in_inorder - inorder_l

            node = TreeNode(cur)
            node.left = dfs(index + 1, inorder_l, cur_pos_in_inorder - 1)
            node.right = dfs(index + 1 + left_size, cur_pos_in_inorder + 1, inorder_r)

            return node

        return dfs(0, 0, len(inorder) - 1)