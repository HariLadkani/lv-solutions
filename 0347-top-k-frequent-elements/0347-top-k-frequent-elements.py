class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        first count freq of nums in a hashmap
        put values of map into heap of size k

        '''

        min_heap = []
        freq_map = {}
        res = []

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        for key, value in freq_map.items():
            heapq.heappush(min_heap, (value, key))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])

        return res