class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        '''
        maximize sum of three values from y array for indices in x array where i,j,k values are distinct in x array
        return -1 if no such triplet
        x = [1,2,1,3,2], y = [5,3,4,6,2]
                   i
        1: 5
        2: 3
        3: 6
        
        (6,5,3)


        

        [1,1,2,2,3]
         i   j   k

         [1,2,1,2] [4,5,6,7]

        '''
        hash_map = defaultdict(int)
     
        for index, num in enumerate(x):
            hash_map[num] = max(hash_map[num], y[index])


        if len(hash_map.keys()) < 3:
            return -1

        heap = [-i for i in hash_map.values()]
        print(heap)
        heapq.heapify(heap)

        first_value = -heapq.heappop(heap)
        second_value = -heapq.heappop(heap) 
        third_value = -heapq.heappop(heap)

        return first_value + second_value + third_value       
