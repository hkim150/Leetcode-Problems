/**
 * @param {number} capacity
 */
var Node = function(key=null, val=null, prev=null, next=null) {
    this.key = key;
    this.val = val;
    this.prev = prev;
    this.next = next;
}

var LRUCache = function(capacity) {
    this.capacity = capacity;
    this.hash = {};
    this.head = null;
    this.tail = null;
    this.size = 0;
    this.pop_last = function() {
        delete this.hash[this.tail.key];
        if (this.size === 1) {
            this.head = null;
            this.tail = null;
        } else {
            this.tail = this.tail.prev;
            this.tail.next = null;
        }
        this.size--;
    }
    
    this.insert_first = function(node) {
        if (this.size === 0) {
            this.head = node;
            this.tail = node;
        } else {
            this.head.prev = node;
            node.next = this.head;
            this.head = node;
        }
        this.size++;
    }
    
    this.move_to_first = function(node) {
        if (node === this.head) {
            return;
        }
        node.prev.next = node.next;
        if (node === this.tail) {
            this.tail = node.prev;
        }
        else {
            node.next.prev = node.prev;
        }
        node.prev = null;
        node.next = this.head;
        this.head.prev = node;
        this.head = node;
    }
};

/** 
 * @param {number} key
 * @return {number}
 */
LRUCache.prototype.get = function(key) {
    if (this.hash.hasOwnProperty(key)) {
        let node = this.hash[key];
        this.move_to_first(node);
        return node.val;
    }
    
    return -1;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LRUCache.prototype.put = function(key, value) {
    if (this.hash.hasOwnProperty(key)) {
        let node = this.hash[key];
        this.move_to_first(node);
        node.val = value;
    } else {
        if (this.size === this.capacity) {
            this.pop_last();
        }
        let newNode = new Node(key, value);
        this.hash[key] = newNode;
        this.insert_first(newNode);
    }
};

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */