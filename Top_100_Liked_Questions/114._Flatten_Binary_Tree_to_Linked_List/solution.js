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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
    if (!root) {
        return;
    }
    
    let flatten_and_return_leaf_node = function(node) {
        if (!node.left && !node.right) {
            return node;
        }
        
        if (!node.left) {
            return flatten_and_return_leaf_node(node.right);
        }
        
        if (!node.right) {
            [node.left, node.right] = [null, node.left];
            return flatten_and_return_leaf_node(node.right);
        }
        
        let left_leaf = flatten_and_return_leaf_node(node.left);
        let right_leaf = flatten_and_return_leaf_node(node.right);
        
        [node.left, left_leaf.right, node.right] = [null, node.right, node.left];
        return right_leaf;
    }
    
    flatten_and_return_leaf_node(root);
};