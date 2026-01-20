class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        goal:
            Maximize number of points
        
        operations can be performed infinite
        
        [3,4,2]
        3: 1
        4: 1
        2: 1
        [11, 10, 10]
        
        RES = 20
        (20, 10, 2)
        (11, 11, 1)

        RES = 4 + 2 

        4 => 3 and 5

        [2,2,3,3,3,4]
        2: 2
        3: 3
        4: 1

        [2,2,3,3,3,4, 6]
        [3,3,6]
        res = 3  + 6 + 3 + 3
        2: 2
        3: 3
        4: 1
        6: 1

        (4, 4, 1) res = 4  => delete(3, 5)
        (10, 1, 10)
        (4, 2, 2)
        
         #(product, value, freq)

        res = 9 + 6 
        delete_set = {2, 4}

        approach:
            maintain a max heap
            delete set to keep track of deletions

        [2,3,6]

        [(2,2), (3, 3), (6, 6)]
         

        [2,2,3,3,3,4]

        [(2, 4), (3, 9), (4, 4)]
          4        9       9

        max(current_sum, previous sum, current + previious if abs diff > 1 between numbers)
        [1,2,3,4,5] = 5 + 3 + 1 = 9
         9 8 8 5 5

        [2,2,,3,3, 3,4]

        {
            2: 4
            3: 3
            4: 1
            0: 0
            1: 0
        }

        dp[0] = 0
        dp[1] = 0
        dp[2] = max(dp[1], 4 + dp[0]) = 4
        dp[3] = max(dp[2], map[3]+dp[1]) = 9
        dp[4] = max(dp[3], map[4]+dp[2]) = 9, 8 = 9
        returnn dp[-1]
        '''
        dp = {}
        dp[-1] = 0
        dp[0]= 0

        num_to_freq = Counter(nums)
        max_value = max(nums)

        for index in range(1, max_value+1):
            dp[index] = max(dp[index-1], num_to_freq[index]*index + dp[index-2])


        return dp[max_value]
    

            


        
        
        