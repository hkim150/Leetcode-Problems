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
    public int kthSmallest(TreeNode root, int k) {
        LinkedList<TreeNode> stack = new LinkedList<TreeNode>();

        while (true) {
            while (root != null) {
                stack.add(root);
                root = root.left;
            }

            root = stack.removeLast();

            if (--k == 0) return root.val;
            root = root.right;
        }
    }
}

class Solution2 {
    public List<Integer> getInorderList(TreeNode root, List<Integer> list) {
        if (root == null)
            return list;

        this.getInorderList(root.left, list);
        list.add(root.val);
        this.getInorderList(root.right, list);
        return list;
    }

    public int kthSmallest(TreeNode root, int k) {
        List<Integer> inorderList = this.getInorderList(root, new ArrayList<Integer>());
        return inorderList.get(k - 1);
    }
}