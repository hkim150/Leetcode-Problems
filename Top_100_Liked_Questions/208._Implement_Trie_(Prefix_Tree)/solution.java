class Trie {
    public Node head;

    /** Initialize your data structure here. */
    public Trie() {
        this.head = new Node('_');
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        Node curr = this.head;
        for (int i=0; i<word.length(); i++) {
            int idx = (int) word.charAt(i) - (int) 'a';
            if (curr.children[idx] == null)
                curr.children[idx] = new Node(word.charAt(i));

            curr = curr.children[idx];
        }

        curr.isEnd = true;
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        Node curr = this.head;
        for (int i=0; i<word.length(); i++) {
            curr = curr.children[(int) word.charAt(i) - (int) 'a'];
            if (curr == null)
                return false;
        }

        return curr.isEnd;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        Node curr = this.head;
        for (int i=0; i<prefix.length(); i++) {
            curr = curr.children[(int) prefix.charAt(i) - (int) 'a'];
            if (curr == null) {
                return false;
            }
        }

        return true;
    }
}

class Node {
    public char letter;
    public Node[] children;
    public boolean isEnd;

    public Node(char ch, boolean isEnd) {
        this.letter = ch;
        this.children = new Node[26];
        this.isEnd = isEnd;
    }

    public Node(char ch) {
        this(ch, false);
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */