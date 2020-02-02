class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v1d = []
        listType = type([])
        for elem in v:
            if type(elem) == listType:
                self.v1d.extend(elem)
            else:
                self.v1d.append(elem)

    def next(self) -> int:
        return self.v1d.pop(0)

    def hasNext(self) -> bool:
        return len(self.v1d) >= 1


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()