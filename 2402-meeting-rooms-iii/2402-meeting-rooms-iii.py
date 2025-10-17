class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        '''
        lowest available room number
        duration stays same for meeting
        give priority to early start meetings

        goal:
            Room NUMBER with most meetings
            return one with lowest if more than one

        Questions?
        Length of input meetings? 10^5
        mininum size meetings? 1
        range of n? 1 to 100

        [[0,10],[1,5],[2,7],[3,4]]

        0: 0
        1: 0
        available = [] #(room)
        occupied = [(10, 0), (5, 1)]





        approach:
                SORT INPUT on start time
                maintain two min heaps
                    one for available(has room number) 
                    one for occupied(end_time, roomnumber)

                pop from occupied based on start time and push to availble
                if available still not populated, force pop from occupied
                update start time accordinly and keep duration same

        '''
        available = [] #(room Number)
        occupied = [] #(end_time, room number)
        room_map = defaultdict(int) #room number: count of meetings
        meetings.sort()

        for r_m in range(n):
            heapq.heappush(available, r_m)

        for start, end in meetings:
            while occupied and occupied[0][0] <= start:
                end_time, room_number = heapq.heappop(occupied)
                heapq.heappush(available, room_number)

            if not available:
                end_time, room_number = occupied[0]
                while occupied and end_time == occupied[0][0]:
                    heapq.heappush(available, heapq.heappop(occupied)[1])
                end = end_time + (end-start)

            room_number = heapq.heappop(available)
            room_map[room_number] += 1

            heapq.heappush(occupied, [end, room_number])
            
        print(room_map)
        freq =float("-inf")
        res = None
        for key, value in sorted(room_map.items()):
            if value > freq:
                freq = value
                res = key

        return res

