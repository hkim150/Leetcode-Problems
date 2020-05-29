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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    // iterative inorder traversal
    let ans = [];
    let q = [[root, 0]];
    
    while (q.length) {
        let [node, lvl] = q.shift();
        
        if (!node)
            continue
        
        if (ans.length === lvl)
            ans.push([]);
        
        ans[lvl].push(node.val);
        
        q.push([node.left, lvl+1]);
        q.push([node.right, lvl+1]);
    }
    
    return ans;
}

var levelOrder2 = function(root) {
    // recursive inorder traversal
    let ans = [];
    let helper = function(node, lvl) {
        if (!node)
            return
        
        if (ans.length === lvl)
            ans.push([]);
        
        ans[lvl].push(node.val);
        
        helper(node.left, lvl+1);
        helper(node.right, lvl+1);
    }
    
    helper(root, 0);
    return ans;
};