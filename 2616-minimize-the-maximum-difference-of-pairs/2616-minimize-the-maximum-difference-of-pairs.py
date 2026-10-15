class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        '''

        [1, 1, 2, 3, 7, 10]

        [1,3, 3, 4] p = 2

        [1,2,2,4]
        l 
                r
        p = 1
        0 1 2 3
        l     r
        left 0
        right 3
        mid 1
        index 0
        diff 1
        pairs_formed 1
        #########
        index 2
        diff 2
        pairs_formed 1
        valid
        res 1
        '''
        nums.sort()

        def valid(target):
            pairs_formed = 0
            i = 0
            while i < len(nums)-1:
                if abs(nums[i] - nums[i+1]) > target:
                    i += 1
                    continue

                pairs_formed += 1
                i += 2
           

            return pairs_formed >= p

                

        max_diff = nums[len(nums)-1] - nums[0]
        left = 0
        right= max_diff
        res = float("inf")
   
        while left <= right:
            mid = (left + right) // 2
      
            if valid(mid):
            
                res = min(res, mid)
                right = mid - 1
          

            else:
                
                left = mid + 1


        return res
