class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        '''
        constraint: divide balls such that each bag has > 0 balls
                maxOperations
        goal:
            distribute balls across bags 
            minimize max balls in a bag
        log(maxOperations) reduction

        9: 1, 8
        9: 2, 7
        9: 3, 6
        9: 4, 5

        0 1 2
    i   9 5

        1 2 3 4 5 6 7 8 9 10
            l
                
              r


        answer=5 (5 is max value in nums)

        [9] 2 operations
        [4,5]

        answer=2 (2 is max value in nums)
        9 / 2 = 4,5
        5/2 = 3,2


        answer = 3 (3 is max value in nums)
        9 / 2 = 4,5
        5 / 2 = 3,2

        [2,4,8,2], maxOperations = 4
         
        1 2 3 4 5 6 7 8
        l
            r

        [2,3,8,2]
               i
        operation = 3
        answer = 4
        8/2 = 4,4

        answer = 2
        maxOperations = 0
        [2,3,8,2]
                 i
        3/2 = 1,2
        8/2 = 4, 4
        4/2 = 2
        4/2 = 2

        [9]

        left 1
        right 9
        min penalty 5
        num 9
        operations_left 2
        operations_left 1
        valid True
        res 5
        #########
        left 1
        right 4
        min penalty 2
        num 9
        operations_left 2
        operations_left -2
        res 5
        #########
        left 3
        right 4
        min penalty 3
        num 9
        operations_left 2
        operations_left -1
        res 5
        #########
        left 4
        right 4
        min penalty 4
        num 9
        operations_left 2
        operations_left 0
        valid True
        res 4
        #########

        '''
        left = 1
        right = max(nums)
        res = float("inf")

        def valid(maximum_allowed):
            operations_left = maxOperations
            
            for i, num in enumerate(nums):
  
                if num <= maximum_allowed:
                    continue
                
              
                operation_consumed =  (num // maximum_allowed)
                remainder = num % maximum_allowed

                if remainder == 0:
                    operation_consumed -= 1

                operations_left -= operation_consumed

               

            return True if operations_left >= 0 else False
        

        while left <= right:
        
            min_penalty = (left+right)//2
          

            if valid(min_penalty):
                right = min_penalty - 1
                res = min(min_penalty, res)
                
            else:
                left = min_penalty + 1
      

        return res