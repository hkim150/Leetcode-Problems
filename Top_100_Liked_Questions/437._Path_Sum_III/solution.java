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
    public int count;
    public int sum;
    public Map<Integer, Integer> map;

    public int pathSum(TreeNode root, int sum) {
        this.count = 0;
        this.sum = sum;
        this.map = new HashMap<Integer, Integer>();
        this.preorder(root, 0);
        return this.count;
    }

    public void preorder(TreeNode node, int currSum) {
        if (node == null)
            return;

        currSum += node.val;
        if (currSum == this.sum)
            this.count++;

        this.count += this.map.getOrDefault(currSum - this.sum, 0);
        this.map.put(currSum, this.map.getOrDefault(currSum, 0) + 1);

        this.preorder(node.left, currSum);
        this.preorder(node.right, currSum);

        this.map.put(currSum, this.map.get(currSum)-1);
    }
}


class Solution2 {
    public int count;

    public int pathSum(TreeNode root, int sum) {
        this.count = 0;
        this.pathSum(root, sum, new ArrayList<>());
        return this.count;
    }

    public void pathSum(TreeNode root, int sum, List<Integer> lst) {
        if (root == null)
            return;

        lst.add(0);
        for (int i=0; i<lst.size(); i++) {
            int s = lst.get(i) + root.val;
            if (s == sum)
                this.count++;

            lst.set(i, s);
        }

        this.pathSum(root.left, sum, new ArrayList<Integer>(lst));
        this.pathSum(root.right, sum, new ArrayList<Integer>(lst));
    }
}