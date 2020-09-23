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
    public boolean isValidBST(TreeNode root) {
        Stack<BSTState> stack = new Stack<>();
        stack.push(new BSTState(root, null, null));

        while (!stack.isEmpty()) {
            BSTState state = stack.pop();
            TreeNode node = state.node;
            Integer leftBound = state.leftBound;
            Integer rightBound = state.rightBound;

            if (node == null)
                continue;

            if (leftBound != null && leftBound >= node.val)
                return false;

            if (rightBound != null && rightBound <= node.val)
                return false;

            stack.push(new BSTState(node.left, leftBound, node.val));
            stack.push(new BSTState(node.right, node.val, rightBound));
        }

        return true;
    }
}

class BSTState {
    public TreeNode node;
    public Integer leftBound;
    public Integer rightBound;

    public BSTState(TreeNode node, Integer leftBound, Integer rightBound) {
        this.node = node;
        this.leftBound = leftBound;
        this.rightBound = rightBound;
    }

    public BSTState() {
        this(null, null, null);
    }
}


class Solution2 {
    public boolean isValidBST(TreeNode root) {
        return helper(root, null, null);
    }

    public boolean helper(TreeNode node, Integer leftBound, Integer rightBound) {
        if (node == null)
            return true;

        if (leftBound != null && leftBound >= node.val)
            return false;

        if (rightBound != null && rightBound <= node.val)
            return false;

        return helper(node.left, leftBound, node.val) && helper(node.right, node.val, rightBound);
    }
}