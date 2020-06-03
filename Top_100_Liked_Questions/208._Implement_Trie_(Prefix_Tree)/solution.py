class TrieNode:
    
    def __init__(self):
        self.links = [None] * 26
        self.end = False

    def get(self, ch):
        return self.links[self.ch2Int(ch)]
    
    def containsKey(self, ch):
        return self.get(ch) is not None
    
    def put(self, ch, node):
        self.links[self.ch2Int(ch)] = node
    
    def ch2Int(self, ch):
        return ord(ch) - ord('a')
    
    def isEnd(self):
        return self.end
    
    def setEnd(self):
        self.end = True
        
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        
        node.setEnd()

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            
            node = node.get(ch)
        
        return node.isEnd()

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                return False
            
            node = node.get(ch)
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)