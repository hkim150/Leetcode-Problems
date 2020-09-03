/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lca;

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        this.lca = null;
        this.helper(root, p, q);
        return this.lca;
    }

    public boolean helper(TreeNode node, TreeNode p, TreeNode q){
        if (node == null)
            return false;

        boolean left = helper(node.left, p, q);
        boolean right = helper(node.right, p, q);
        boolean either = (node == p) || (node == q);

        if ( (left ? 1 : 0) + (right ? 1 : 0) + (either ? 1 : 0) >= 2 )
            this.lca = node;

        return left || right || either;
    }
}


class Solution2 {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return this.helper(root, p, q).lca;
    }

    public Triplet helper(TreeNode node, TreeNode p, TreeNode q) {
        if (node == null)
            return new Triplet();

        Triplet tl = helper(node.left, p, q);
        Triplet tr = helper(node.right, p, q);

        if (tl.lca != null)
            return tl;
        if (tr.lca != null)
            return tr;

        boolean has_p = tl.has_p || tr.has_p || node == p;
        boolean has_q = tl.has_q || tr.has_q || node == q;
        TreeNode lca = has_p && has_q ? node : null;
        return new Triplet(has_p, has_q, lca);
    }
}

class Triplet {
    public boolean has_p;
    public boolean has_q;
    public TreeNode lca;

    public Triplet(boolean has_p, boolean has_q, TreeNode lca) {
        this.has_p = has_p;
        this.has_q = has_q;
        this.lca = lca;
    }

    public Triplet() {
        this.has_p = false;
        this.has_q = false;
        this.lca = null;
    }
}