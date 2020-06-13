/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    // recursive post order traversal
    let ans = [null];
    let helper = function(node) {
        if (!node) {
            return false;
        }
        
        let left = helper(node.left);
        let right = helper(node.right);
        
        let mid = (node === p || node === q);
        
        if (mid + left + right >= 2) {
            ans[0] = node;
        }
        
        return mid || left || right;
    }
    
    helper(root);
    return ans[0];
}

var lowestCommonAncestor2 = function(root, p, q) {
    // find the index of the p and q as if the tree is in the array form
    if (root == null) {
        return null;
    }
    
    let p_idx = null;
    let q_idx = null;
    let queue = [[root, 0]];
    while (queue.length && (p_idx == null || q_idx == null)) {
        let [node, idx] = queue.shift();
        if (node.val === p.val) {
            p_idx = idx;
        } else if (node.val === q.val) {
            q_idx = idx;
        }
        
        if (node.left != null) {
            queue.push([node.left, idx*2+1]);
        }
        if (node.right != null) {
            queue.push([node.right, idx*2+2]);
        }
    }
    
    // get the parent index of the bigger one until the indices match
    while (p_idx != q_idx) {
        if (p_idx < q_idx) {
            q_idx = Math.floor((q_idx-1)/2);
        } else {
            p_idx = Math.floor((p_idx-1)/2);
        }
    }
    
    let lca_idx = p_idx;
    if (lca_idx === 0) {
        return root;
    }
    
    // with the lca index, get the path to the root node
    let path = [];
    while (lca_idx > 0) {
        path.push(lca_idx);
        lca_idx = Math.floor((lca_idx-1)/2);
    }
    
    // reverse traverse the path and return the node object
    let idx = 0;
    let ansNode = root;
    for (let p of path.reverse()) {
        if (p === idx*2+1) {
            ansNode = ansNode.left;
            idx = idx*2+1;
        } else {
            ansNode = ansNode.right;
            idx = idx*2+2;
        }
    }
    
    return ansNode;
};