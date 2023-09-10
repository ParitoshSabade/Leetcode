import heapq
class MinStack:

    def __init__(self):
        self.stck = []

    def push(self, val: int) -> None:
        self.stck.append(val)
        return None

    def pop(self) -> None:
        self.stck.pop()
        

    def top(self) -> int:
        return self.stck[-1]
        

    def getMin(self) -> int:
        return min(self.stck)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()