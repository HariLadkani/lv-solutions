class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        [2,3,1,1,4]
         i  i  i  i  

         0 1 2 3 4
        [3,2,1,0,4]

       


        [2,3,1,1,4]




        [2,3,1,1,4]
        
        

        [3,2,1,0,4]

        [2,3,1,1,4]

        '''

        q = deque([0])
        last_processed = 0
        while q:
            current_index = q.popleft()

            if current_index == len(nums)-1:
                return True

            min_index = max(current_index + 1, last_processed+1)
            max_index = current_index + nums[current_index]

            for r in range(min_index, max_index+1):
                q.append(r)

            last_processed = max(last_processed, max_index)


        return False

