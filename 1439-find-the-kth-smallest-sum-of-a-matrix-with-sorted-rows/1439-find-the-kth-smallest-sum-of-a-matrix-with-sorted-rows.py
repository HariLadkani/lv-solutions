class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        '''
        i
        1 4 11
        2 4 6
          i
        
        sum = 3, 5, 7
        (1, 4)
        (1, 6)


        compute sum from adding all first elements
        add all first element of them to max heap
        pop maximum, substract from curr sum, find its next element in array and add it
        maintain a counter.
        loop till counter < k

      

        goal:
            kth smallest sum 
        
        constraints:
            EXACTLY one element from each row 

        Approach:
            

        '''
        min_heap = []
        curr_sum = 0

        for i, l in enumerate(mat):
            curr_sum += l[0]
            
        indices = [0] * len(mat)
        heapq.heappush(min_heap, (curr_sum, tuple(indices)))
        counter = 0
        visit = set()

        while min_heap:
            
            curr_sum, indices = heapq.heappop(min_heap)
            if indices in visit:
                continue
            counter += 1
            if counter == k:
                return curr_sum

            visit.add(indices)

            

            indices = list(indices)
            #0, 0
            for row in range(len(indices)):
                index = indices[row]
                if index == len(mat[row]) - 1:
                    continue

                temp_sum = curr_sum
                temp_sum -= mat[row][index]
                indices[row] += 1
                temp_sum += mat[row][indices[row]]
                heapq.heappush(min_heap, (temp_sum, tuple(indices)))
                indices[row] -= 1

                


        