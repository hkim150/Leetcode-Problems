/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function(root) {
    if (!root) {
        return 0;
    }
    
    let ans = -1;
    const maxDepth = root => {
        if (!root) {
            return -1;
        }
        const L = maxDepth(root.left);
        const R = maxDepth(root.right);
        ans = Math.max(ans, 2 + L + R);
        return 1 + Math.max(L, R);
    }
    
    maxDepth(root);
    
    return ans;
};