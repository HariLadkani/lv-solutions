class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
        
class MyCircularQueue:

    def __init__(self, k: int):
        '''
        last position connected to first position
        
        ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue",                 "Rear"]
        
        [[3], [1], [2], [3], [4], [], [], [], [4], []]
        
        Output
        [null, true, true, true, false, 3, true, true, true, 4]
        
        [1, 2, 3]
         l 
                r
                
        head => Node <=tail
        '''
        self.size = 0
        self.maxSize = k
        
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.next = self.head
        
        

    def enQueue(self, value: int) -> bool:
        if self.size >= self.maxSize:
            return False
        
        new_node = Node(value=value)
        
        node_tail_points_to = self.tail.next #head
        node_tail_points_to.next = new_node #
        self.tail.next = new_node
        self.size += 1
     
        return True

    def deQueue(self) -> bool:
        '''
        pop from front
        '''
        if self.head.next == self.tail:
            return False
        print(f"dequed: {self.head.next.value}")
       
        self.head.next = self.head.next.next
        if not self.head.next:
            self.head.next = self.tail
            self.tail.next = self.head
        self.size -= 1


        return True
        
        
        

    def Front(self) -> int:
        if self.head.next == self.tail:
            return -1
        
        return self.head.next.value
            
        

    def Rear(self) -> int:
        if self.head.next == self.tail:
            print("head == tail")
            return -1
        
        return self.tail.next.value

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def isFull(self) -> bool:
        return self.size == self.maxSize
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()