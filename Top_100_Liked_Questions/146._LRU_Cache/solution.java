class LRUCache {

    private int size;
    private int capacity;
    private Node LRU_head;
    private Node LRU_tail;
    private Map<Integer, Node> map;

    public LRUCache(int capacity) {
        this.size = 0;
        this.capacity = capacity;
        this.LRU_head = new Node(0, 0);
        this.LRU_tail = new Node(0, 0, this.LRU_head, null);
        this.LRU_head.next = this.LRU_tail;
        this.map = new HashMap<Integer, Node>();
    }

    public int get(int key) {
        if (this.size == 0 || !this.map.containsKey(key))
            return -1;

        Node node = this.map.get(key);

        if (this.LRU_head.next != node) {
            // remove the node from the linked list
            node.prev.next = node.next;
            node.next.prev = node.prev;

            // put the node at the front of the linked list
            node.next = this.LRU_head.next;
            this.LRU_head.next = node;

            node.next.prev = node;
            node.prev = this.LRU_head;
        }

        return node.val;
    }

    public void put(int key, int value) {
        if (this.map.containsKey(key)) {
            Node node = this.map.get(key);

            if (this.LRU_head.next != node) {
                // remove the node from the linked list
                node.prev.next = node.next;
                node.next.prev = node.prev;

                // put the node at the front of the linked list
                node.next = this.LRU_head.next;
                this.LRU_head.next = node;

                node.next.prev = node;
                node.prev = this.LRU_head;
            }

            node.val = value;
        } else {
            if (this.size == this.capacity) {
                // evict the lru
                Node evictNode = this.LRU_tail.prev;
                this.LRU_tail.prev = evictNode.prev;
                evictNode.prev.next = this.LRU_tail;

                this.map.remove(evictNode.key);
                this.size--;
            }

            // create a new node and put it in the map
            Node node = new Node(key, value);
            this.map.put(key, node);

            // put the node at the front of the linked list
            node.next = this.LRU_head.next;
            this.LRU_head.next = node;

            node.next.prev = node;
            node.prev = this.LRU_head;

            this.size++;
        }
    }
}


class Node {
    public int key;
    public int val;
    public Node prev;
    public Node next;

    public Node(int key, int val, Node prev, Node next) {
        this.key = key;
        this.val = val;
        this.prev = prev;
        this.next = next;
    }

    public Node(int key, int value) {
        this(key, value, null, null);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */