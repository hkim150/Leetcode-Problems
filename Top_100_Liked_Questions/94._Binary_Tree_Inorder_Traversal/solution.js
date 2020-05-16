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
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    let stack = [];
    let node = root;
    let ans = [];
    
    while (node || stack.length) {
        // left
        while (node) {
            stack.push(node);
            node = node.left;
        }
        // head
        node = stack.pop();
        ans.push(node.val);
        // right
        node = node.right;
    }
    
    return ans;
}

var inorderTraversal2 = function(root) {
    let ans = [];
    
    let helper = function(node) {
        if (!node) {
            return;
        }
        
        // inorder - left -> head -> right
        helper(node.left);
        ans.push(node.val);
        helper(node.right);
    }
    
    helper(root);
    
    return ans;
};