class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''

        goal:
            return array of maximum of window size k in nums

        nlogk

        '''
        to_delete = set()
        res = []
        max_heap = []
        for i in range(len(nums)):
            while max_heap and max_heap[0][1] in to_delete:
                heapq.heappop(max_heap)

            heapq.heappush(max_heap, (-nums[i], i))

            if i + 1 >= k:
                res.append(-max_heap[0][0])
                to_delete.add(i+1-k)

        return res


