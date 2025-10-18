class BST:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.leftChild = None
        self.rightChild = None

    def insert(self, start_time, end_time):

        curr = self

        while True:
            if start_time >= curr.end:
                if not curr.rightChild:
                    curr.rightChild = BST(start_time, end_time)
                    return True
                
                curr = curr.rightChild

            elif end_time <= curr.start:
                if not curr.leftChild:
                    curr.leftChild  = BST(start_time, end_time)
                    return True

                curr = curr.leftChild

            else:
                return False
        


class MyCalendar:

    def __init__(self):
        self.root = None
        
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = BST(startTime, endTime)
            return True

        if self.root.insert(startTime, endTime):
            return True

        return False
        

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)