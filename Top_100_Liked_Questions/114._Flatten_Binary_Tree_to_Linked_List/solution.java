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
    public void flatten(TreeNode root) {
        if (root != null)
            this.flatten_and_return_leaf(root);
    }

    public TreeNode flatten_and_return_leaf(TreeNode root) {
        if (root.left == null && root.right == null)
            return root;

        if (root.left == null)
            return this.flatten_and_return_leaf(root.right);

        if (root.right == null) {
            root.right = root.left;
            root.left = null;
            return this.flatten_and_return_leaf(root.right);
        }

        TreeNode leftLeaf = this.flatten_and_return_leaf(root.left);
        leftLeaf.right = root.right;
        root.right = root.left;
        root.left = null;
        return this.flatten_and_return_leaf(leftLeaf.right);
    }
}


class Solution2 {
    public List<TreeNode> nodes;

    public void flatten(TreeNode root) {
        this.nodes = new ArrayList<>();
        this.preOrder(root);

        for (int i=0; i<this.nodes.size()-1; i++) {
            TreeNode node = this.nodes.get(i);
            node.left = null;
            node.right = this.nodes.get(i+1);
        }
    }

    public void preOrder(TreeNode root) {
        if (root == null)
            return;

        this.nodes.add(root);
        this.preOrder(root.left);
        this.preOrder(root.right);
    }
}