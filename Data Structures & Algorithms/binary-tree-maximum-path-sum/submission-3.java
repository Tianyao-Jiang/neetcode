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
    // brute force 
    int result = -1001;

    public int maxPathSum(TreeNode root) {
        dfs(root);

        return result;
    }

    private int getMax(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int maxLeft = getMax(root.left);
        int maxRight = getMax(root.right);
        int res = root.val + Math.max(maxLeft, maxRight);
        return Math.max(0, res);
    }

    private void dfs(TreeNode root) {
        if (root == null) {
            return;
        }

        int maxLeft = getMax(root.left);
        int maxRight = getMax(root.right);
        int curResult = root.val + maxLeft + maxRight;

        result = Math.max(result, curResult);

        dfs(root.left);
        dfs(root.right);
    }
}
