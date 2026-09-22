class SeatManager:

    def __init__(self, n: int):
        '''
        5 seats to start with

        5
        
        '''
        self.min_heap = [n for n in range(1, n+1)]
        heapq.heapify(self.min_heap)
        

    def reserve(self) -> int:
        '''
        pick smallest unreserved seat
        pop it and return it
        '''
        return heapq.heappop(self.min_heap)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.min_heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)