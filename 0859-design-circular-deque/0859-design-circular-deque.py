class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.limit = k
        self.front = None
        self.last = None

    def insertFront(self, value: int) -> bool:
        if self.size == self.limit:
            return False
        node = Node(value)
        if self.size == 0: 
            self.front = self.last = node
            node.next = node.prev = node 
        else:
            self.front.prev = node
            node.next = self.front
            node.prev = self.last
            self.last.next = node
            self.front = node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.limit:
            return False
        node = Node(value)
        if self.size == 0:
            self.front = self.last = node
            node.next = node.prev = node 
        else:
            self.last.next = node
            node.prev = self.last
            node.next = self.front
            self.front.prev = node
            self.last = node
        self.size += 1
        return True
        
    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:  
            self.front = self.last = None
        else:
            self.front.next.prev = self.last
            self.last.next = self.front.next
            self.front = self.front.next
        self.size -= 1
        return True


    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:  
            self.front = self.last = None
        else:
            self.last.prev.next = self.front
            self.front.prev = self.last.prev
            self.last = self.last.prev
        self.size -= 1
        return True
        

    def getFront(self) -> int:
        if self.front:
            return self.front.val
        return -1
        

    def getRear(self) -> int:
        if self.last:
            return self.last.val
        return -1
        

    def isEmpty(self) -> bool:
        if self.front == self.last == None:
            return True
        return False
    def isFull(self) -> bool:
        if self.size == self.limit:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()