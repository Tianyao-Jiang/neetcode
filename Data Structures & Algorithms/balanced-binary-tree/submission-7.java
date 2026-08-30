/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isBalanced(TreeNode root) {

        int[] res = new int[]{0};
        dfs(root, res);

        return res[0] != 1;
    }

    private int dfs(TreeNode root, int[] res) {
        if (root == null) {
            return 0;
        }

        int leftHeight = dfs(root.left, res);
        int rightHeight = dfs(root.right, res);

        if (Math.abs(leftHeight - rightHeight) > 1) {
            res[0] = 1;
        }

        return 1 + Math.max(leftHeight, rightHeight);
    }
}
