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
        boolean[] res = new boolean[]{true};

        dfs(root, res);

        return res[0];
    }

    private int dfs(TreeNode root, boolean[] res) {
        if (root == null) {
            return 0;
        }

        int leftH = dfs(root.left, res);
        int rightH = dfs(root.right, res);

        if (Math.abs(leftH - rightH) > 1) {
            res[0] = false;
        }
        
        return 1 + Math.max(leftH, rightH);
    }
}
