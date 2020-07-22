class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.moves = [0] * size
        self.curr_size = 0
        self.max_size = size
        self.idx = 0
        self.total = 0

    def next(self, val: int) -> float:
        self.total -= self.moves[self.idx]
        self.total += val
        self.moves[self.idx] = val
        self.idx = (self.idx + 1) % self.max_size
        
        if self.curr_size < self.max_size:
            self.curr_size += 1
        
        return self.total / self.curr_size
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)