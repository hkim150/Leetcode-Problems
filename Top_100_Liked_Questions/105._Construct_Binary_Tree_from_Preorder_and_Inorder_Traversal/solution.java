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
    public int[] preorder;
    public int[] inorder;
    public int preorder_idx;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        this.preorder_idx = 0;

        return this.findNodeFromInorderAndConnect(0, inorder.length);
    }

    public TreeNode findNodeFromInorderAndConnect(int left, int right) {
        if (left >= right)
            return null;

        int inorder_idx = -1;
        int preorder_val = this.preorder[this.preorder_idx++];

        for (int i=left; i<right; i++) {
            if (this.inorder[i] == preorder_val) {
                inorder_idx = i;
                break;
            }
        }

        TreeNode node = new TreeNode(preorder_val);
        node.left = this.findNodeFromInorderAndConnect(left, inorder_idx);
        node.right = this.findNodeFromInorderAndConnect(inorder_idx+1, right);

        return node;
    }
}