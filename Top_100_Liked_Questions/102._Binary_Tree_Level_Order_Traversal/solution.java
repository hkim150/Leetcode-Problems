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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ans = new ArrayList<>();

        if (root == null)
            return ans;

        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(0, root));

        while (!q.isEmpty()) {
            Pair pair = q.poll();

            if (ans.size() == pair.level)
                ans.add(new ArrayList<Integer>());

            List<Integer> list = ans.get(pair.level);
            list.add(pair.node.val);

            if (pair.node.left != null)
                q.add(new Pair(pair.level+1, pair.node.left));

            if (pair.node.right != null)
                q.add(new Pair(pair.level+1, pair.node.right));
        }

        return ans;
    }
}

class Pair {
    public int level;
    public TreeNode node;

    public Pair(int level, TreeNode node) {
        this.level = level;
        this.node = node;
    }

    @Override
    public String toString() {
        return String.format("level: " + this.level + ", node_val: " + this.node.val);
    }
}