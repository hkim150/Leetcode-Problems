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
 * @param {number} sum
 * @return {number}
 */
var pathSum = function(root, sum) {
    if (!root) {
        return 0;
    }
    
    let ans = 0;
    const numPath = (r, s=sum) => {
        if (!r) {
            return
        }
        
        if (r.val === s){
            ans += 1;
        }
        
        numPath(r.left, s - r.val);
        numPath(r.right, s - r.val);
    }
    
//     let currNode = root;
//     const stack = [root];
    
//     while (stack.length) {
//         if (currNode) {
            
//             if (currNode.right) {
//                 stack.push(currNode.right);
//             }
            
//             numPath(currNode);
//             currNode = currNode.left;
//         } else {
//             currNode = stack.pop();
//         }
//     }
    
    const queue = [root];
    while (queue.length) {
        const currNode = queue.shift();
        
        numPath(currNode);
        
        if (currNode.left) {
            queue.push(currNode.left);
        }
        
        if (currNode.right) {
            queue.push(currNode.right);
        }
    }
    
    return ans;
};