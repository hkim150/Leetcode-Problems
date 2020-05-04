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
var isSymmetric = function(root) {
    if (!root) {
        return true;
    }

    const queue = [[root.left, root.right]];
    
    while (queue.length > 0) {
        const [L, R] = queue.shift();
        
        if (!L && !R) {
            continue;
        }
        
        if (!L != !R || L.val != R.val) {
            return false;
        }
        
        queue.push([L.left, R.right]);
        queue.push([L.right, R.left]);
    }
    
    return true;
}


var isSymmetric2 = function(root) {
    if (!root) {
        return true;
    }
    
    const helper = (L, R) =>  {
        if (!L && !R) {
            return true;
        }
        
        if (!!L != !!R) {
            return false;
        }
        
        return L.val == R.val && helper(L.left, R.right) && helper(L.right, R.left);
    }
    
    return helper(root.left, root.right);
};