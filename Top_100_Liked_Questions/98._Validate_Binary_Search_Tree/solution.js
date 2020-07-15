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
 * @return {boolean}
 */
var isValidBST = function(root) {
    // iterative
    let stack = [[root, -Infinity, Infinity]];
    
    while (stack.length) {
        let [node, lb, rb] = stack.pop();
        
        if (!node) {
            continue;
        }
        
        if (lb >= node.val || node.val >= rb) {
            return false;
        }
        
        stack.push([node.left, lb, node.val]);
        stack.push([node.right, node.val, rb]);
    }
    
    return true;
}


var isValidBST2 = function(root) {
    // recursive
    let helper = function(node, lb, rb) {
        if (!node) {
            return true;
        }
        
        return lb < node.val && node.val < rb && helper(node.left, lb, node.val) && helper(node.right, node.val, rb);
    }
    
    return helper(root, -Infinity, Infinity);
};