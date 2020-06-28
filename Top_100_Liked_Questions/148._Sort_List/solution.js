/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function(head) {
    let merge = function(l1, l2) {    
        let retHead;
        if (l1.val < l2.val) {
            retHead = l1;
            l1 = l1.next;
        } else {
            retHead = l2;
            l2 = l2.next;
        }
            
        let curr = retHead;
        while (l1 && l2) {
            if (l1.val < l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        
        if (l1) {
            curr.next = l1;
        }
        if (l2) {
            curr.next = l2;
        }
            
        return retHead;
    }
    
    let mergeSort = function(lst) {
        if (!lst || !lst.next) {
            return lst;
        }
        
        let slow = lst;
        let fast = lst;
        
        while (true) {
            fast = fast.next;
            if (!fast) {
                break;
            }
            fast = fast.next;
            if (!fast) {
                break;
            }
            slow = slow.next;
        }
        
        let lst2 = slow.next;
        slow.next = null;

        let l1 = mergeSort(lst);
        let l2 = mergeSort(lst2);
        return merge(l1, l2);
    }
    
    return mergeSort(head);
};


let printLst = function(lst) {
    if (!lst) {
        return;
    }

    let str = lst.val.toString();
    lst = lst.next;

    while (lst) {
        if (str == "") {

        } else {
            str = str + " -> " + lst.val.toString();
        }
        lst = lst.next;
    }

    console.log(str);
}