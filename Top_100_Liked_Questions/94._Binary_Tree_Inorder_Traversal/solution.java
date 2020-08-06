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
// iterative method
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> ans = new ArrayList<>();

        // while not null push oneself to the stack and go to left child
        TreeNode curr = root;
        while (true) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }

            if (stack.empty())
                break;

            // pop the stack and add its value to the answer list
            curr = stack.pop();
            ans.add(curr.val);

            // go to right and repeat
            curr = curr.right;
        }

        return ans;
    }
}

// recursive method
class Solution2 {
    public List<Integer> ans;

    public List<Integer> inorderTraversal(TreeNode root) {
        this.ans = new ArrayList<>();
        this.helper(root);
        return this.ans;
    }

    public void helper(TreeNode root) {
        if (root == null)
            return;

        this.helper(root.left);
        this.ans.add(root.val);
        this.helper(root.right);
    }
}