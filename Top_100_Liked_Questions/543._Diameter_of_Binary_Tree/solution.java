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
    public class Pair {
        public int maxDepth;
        public int maxDiameter;

        public Pair(int maxDepth, int maxDiameter) {
            this.maxDepth = maxDepth;
            this.maxDiameter = maxDiameter;
        }
    }

    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null)
            return 0;

        return this.helper(root).maxDiameter;
    }

    public Pair helper(TreeNode root) {
        if (root == null)
            return new Pair(-1, -1);

        Pair l = helper(root.left);
        Pair r = helper(root.right);

        int maxDepth = Math.max(l.maxDepth, r.maxDepth) + 1;
        int maxDiameter = Math.max(l.maxDepth + r.maxDepth + 2, Math.max(l.maxDiameter, r.maxDiameter));

        return new Pair(maxDepth, maxDiameter);
    }
}

class Solution2 {
    private int maxDiameter = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        this.helper(root);
        return this.maxDiameter;
    }

    public int helper(TreeNode root) {
        if (root == null)
            return -1;
        // max diameter = max depth left + max depth right + 2
        // max depth = max(max depth left, max depth right)
        int maxDepthLeft = helper(root.left);
        int maxDepthRight = helper(root.right);

        this.maxDiameter = Math.max(this.maxDiameter, maxDepthLeft + maxDepthRight + 2);

        return 1 + Math.max(maxDepthLeft, maxDepthRight);
    }
}