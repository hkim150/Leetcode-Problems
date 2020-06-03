var TrieNode = function() {
    this.links = new Array(26).fill(null);
    this.end = false;
}

TrieNode.prototype.ch2Int = function(ch) {
    return ch.charCodeAt(0) - 'a'.charCodeAt(0);
}

TrieNode.prototype.containsKey = function(ch) {
    return this.get(ch) != null;
}

TrieNode.prototype.get = function(ch) {
    return this.links[this.ch2Int(ch)];
}

TrieNode.prototype.put = function(ch, node) {
    this.links[this.ch2Int(ch)] = node;
}

TrieNode.prototype.isEnd = function() {
    return this.end;
}

TrieNode.prototype.setEnd = function() {
    this.end = true;
}

/**
 * Initialize your data structure here.
 */
var Trie = function() {
    this.root = new TrieNode();
};

/**
 * Inserts a word into the trie. 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let node = this.root;
    for (let ch of word) {
        if (!node.containsKey(ch)) {
            node.put(ch, new TrieNode());
        }
        node = node.get(ch);
    }
    node.setEnd();
};

/**
 * Returns if the word is in the trie. 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let node = this.root;
    for (let ch of word) {
        if (!node.containsKey(ch)) {
            return false;
        }
        node = node.get(ch);
    }
    return node.isEnd();
};

/**
 * Returns if there is any word in the trie that starts with the given prefix. 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.root;
    for (let ch of prefix) {
        if (!node.containsKey(ch)) {
            return false;
        }
        node = node.get(ch);
    }
    return true;
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */