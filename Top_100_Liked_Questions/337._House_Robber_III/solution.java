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
class Pair {
    public int canRob;
    public int cannotRob;

    public Pair(int canRob, int cannotRob) {
        this.canRob = canRob;
        this.cannotRob = cannotRob;
    }
}

class Solution {
    public int rob(TreeNode root) {
        Pair p = this.helper(root);
        return p.canRob;
    }

    public Pair helper(TreeNode root) {
        if (root == null)
            return new Pair(0, 0);

        Pair left = this.helper(root.left);
        Pair right = this.helper(root.right);

        int cannotRob = left.canRob + right.canRob;
        int canRob = Math.max(cannotRob, root.val + left.cannotRob + right.cannotRob);

        return new Pair(canRob, cannotRob);
    }
}


class Solution2 {
    public int rob(TreeNode root) {
        return this.helper(root, true);
    }

    public int helper(TreeNode root, boolean robbable) {
        if (root == null)
            return 0;

        int no_rob = this.helper(root.left, true) + this.helper(root.right, true);
        int rob = robbable ? root.val + this.helper(root.left, false) + this.helper(root.right, false) : 0;

        return Math.max(rob, no_rob);
    }
}