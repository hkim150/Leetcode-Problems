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
 * @param {number[]} to_delete
 * @return {TreeNode[]}
 */
var delNodes = function(root, to_delete) {
    let ans = [];
    let set = {};
    to_delete.forEach(v => set[v] = 0);
    
    let helper = function(root, parent, isLeftChild) {
        if (!root) return;
        
        helper(root.left, root, true);
        helper(root.right, root, false);
        
        if (set.hasOwnProperty(root.val)) {
            if (isLeftChild)
                parent.left = null;
            else
                parent.right = null;
            
            if (root.left)
                ans.push(root.left);
            
            if (root.right)
                ans.push(root.right);
        }
    }
    
    if (!set.hasOwnProperty(root.val))
        ans.push(root);
    
    let dummyParent = new TreeNode(0, root);
    helper(root, dummyParent, true);
    
    return ans;
};