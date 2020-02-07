class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {"isEnd":False}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.root
        for ch in word:
            if ch not in currNode:
                currNode[ch] = {"isEnd":False}
            currNode = currNode[ch]
        
        currNode["isEnd"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode = self.root
        for ch in word:
            if ch in currNode:
                currNode = currNode[ch]
            else:
                return False
        
        return currNode["isEnd"]

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currNode = self.root
        for ch in prefix:
            if ch in currNode:
                currNode = currNode[ch]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)