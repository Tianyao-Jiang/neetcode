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
    int result = -10001;

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return result;
    }

    private int dfs(TreeNode root) {

        if (root == null) {
            return 0;
        }

        int maxLeft = Math.max(dfs(root.left), 0);
        int maxRight = Math.max(dfs(root.right), 0);
        int curResult = root.val + maxLeft + maxRight;
        result = Math.max(result, curResult);
        return root.val + Math.max(maxLeft, maxRight);
    }
}
