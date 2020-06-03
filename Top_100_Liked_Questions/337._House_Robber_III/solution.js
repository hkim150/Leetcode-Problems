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
 * @return {number}
 */
var rob = function(root) {
     // recursive dp - O(n)
     let maxRob = function(node) {
         if (!node) {
             return [0,0];
         }
         
         let [cannotRob_left, canRob_left] = maxRob(node.left);
         let [cannotRob_right, canRob_right] = maxRob(node.right);
         
         cannotRob = canRob_left + canRob_right;
         canRob = Math.max(cannotRob, node.val + cannotRob_left + cannotRob_right);
         
         return [cannotRob, canRob];
     }
     
     return maxRob(root)[1];
 }
 
 var rob3 = function(root) {
     // iterative dp
     let arr = [];
     let treeToArr = function(node, i) {
         if (!node) {
             return;
         }
         
         if (arr.length <= i) {
             for (let j=0; j<i+1-arr.length; j++) {
                 arr.push(null);
             }
         }
         
         arr[i] = node.val;
         
         treeToArr(node.left, i*2+1);
         treeToArr(node.right, i*2+2);
     }
     
     treeToArr(root, 0);
     
     let mem = new Array(arr.length+1);
     
     for (let i=0; i<mem.length; i++) {
         mem[i] = new Array(2).fill(0);
     }
     
     for (let i=arr.length; i>-1; i--) {
         if (!arr[i] && arr[i] != 0) {
             continue;
         }
         
         let left = i*2+1 < arr.length && arr[i*2+1] != null ? i*2+1 : arr.length;
         let right = i*2+2 < arr.length && arr[i*2+2] != null ? i*2+2 : arr.length;
         
         mem[i][0] = mem[left][1] + mem[right][1];
         mem[i][1] = Math.max(mem[i][0], arr[i] + mem[left][0] + mem[right][0]);
     }
     
     return mem[0][1];
 }
 
 var rob2 = function(root) {
     // recursive dp - intuitive
     let maxRob = function(node, canRob) {
         if (!node) {
             return 0;
         }
         
         let noRob = maxRob(node.left, true) + maxRob(node.right, true);
         if (canRob) {
             let rob = node.val + maxRob(node.left, false) + maxRob(node.right, false);
             return Math.max(noRob, rob);
         } else {
             return noRob;
         }
     }
     
     return maxRob(root, true);
 };