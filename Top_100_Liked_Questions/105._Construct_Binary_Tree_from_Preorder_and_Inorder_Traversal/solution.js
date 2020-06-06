/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    let p_idx = 0;
    let helper = function(i_left, i_right) {
        if (i_left >= i_right) {
            return null;
        }
        
        let p_val = preorder[p_idx++];
        let i_idx = null;
        for (let i=i_left; i<i_right; i++) {
            if (inorder[i] === p_val) {
                i_idx = i;
                break;
            }
        }
        
        if (i_idx === null) {
            throw "node in preorder not found in inorder";
        }
        
        let left = helper(i_left, i_idx);
        let right = helper(i_idx+1, i_right);
        
        return new TreeNode(p_val, left, right);
    }
    
    return helper(0, preorder.length);
};

