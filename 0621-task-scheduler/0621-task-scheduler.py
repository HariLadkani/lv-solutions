from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        Input
            tasks = array with letters A to Z
            n = int gap between two same tasks

        constrainst:
            each cpu interval:
                idle
                task completion
            any order of task handling
            GAP of intervals > n between same letter task

        Goal:
            Min number of cpu intervals required to finish all tasks
            minimize idle time to minimize total time

        How to minimize idle:
            space tasks such that most repeated task is prioritized

        Approach:
            maintain a max heap with task: frequency
            heap[element] = [frequency, next_available_time]
            maintain a deque. append to right. pop from front
            in each loop,
                check if cool down over for several task
                pop them from cool down and push to heap and then process

        run time:
            o(nlog26)
        space:
            o(26)
        '''

        waiting = deque([]) #(-freq, next_available_time)
        freq_map = Counter(tasks) #A: 2
        max_heap = []
        current_interval = 1

        for key, freq in freq_map.items():
            waiting.append((-freq, current_interval))

        while max_heap or len(waiting) > 0:

            while waiting and current_interval >= waiting[0][1]: # if wait time elapsed, put to heap
                heapq.heappush(max_heap, waiting[0][0])
                waiting.popleft()

            if not max_heap:
                freq, current_interval = waiting.popleft()
                heapq.heappush(max_heap, freq)

            new_freq = heapq.heappop(max_heap) + 1
            if new_freq != 0:
                waiting.append((new_freq, current_interval + 1 + n))

            if not max_heap and len(waiting) == 0:
                return current_interval
            current_interval += 1

        return current_interval

            
            



            


        