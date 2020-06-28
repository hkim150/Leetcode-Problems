class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.valLst = []
        self.hashIdx = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hashIdx:
            self.hashIdx[val] = len(self.valLst)
            self.valLst.append(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hashIdx:
            idx = self.hashIdx[val]
            tailVal = self.valLst.pop()
            if idx != len(self.valLst):
                self.valLst[idx] = tailVal
                self.hashIdx[tailVal] = idx
            del self.hashIdx[val]
            return True
        
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.valLst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()