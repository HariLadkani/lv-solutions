class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Input: stones with weights

        conditions:
            if two stones equal in weight:
                both destroyed

            if one stone is heavier than other:
                destroy smaller one
                large stone weight = large - small 

        Constraints:
            stones left at end <= 1

        Goal:
            return weight of last remaining stone 
            return 0 if no remaining stone

        store elements in max heap
        pop two largest and apply conditons
        push remaining stones back to heap
        do till len(heap) > 1
        return heap[0] if heap else 0
        run time: O(nlogn)
        space: o(n)

        '''
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap) #[-8, -7,.....]

        while len(max_heap)>1:
            stone_1 = -heapq.heappop(max_heap) #bigger
            stone_2 = -heapq.heappop(max_heap) #smaller

            if stone_1 ==  stone_2:
                continue

            else:
                resulting_stone = stone_1 - stone_2
                heapq.heappush(max_heap, -resulting_stone)

        return -max_heap[0] if max_heap else 0



        

        