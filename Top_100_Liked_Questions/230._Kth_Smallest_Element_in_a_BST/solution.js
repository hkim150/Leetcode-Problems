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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    let stack = [];
    
    while (true) {
        while (root) {
            stack.push(root);
            root = root.left;
        }
        root = stack.pop();
        
        k -= 1;
        if (k === 0) {
            return root.val;
        }
        
        root = root.right;
    }
    throw "answer not found";
}
    
var kthSmallest = function(root, k) {
    let inorder = function(node) {
        return node ? [...inorder(node.left), node.val, ...inorder(node.right)] : [];
    }
    return inorder(root)[k-1];
};