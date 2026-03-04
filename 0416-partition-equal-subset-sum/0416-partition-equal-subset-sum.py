class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''

        if sum is odd, return false
        target sum = 11

                    capacity
    wei    Eleme        0   1   2   3   4   5   6   7   8   9   10  11
    0      0            T   F   F   F   F   F   F   F   F   F   F   F
    1      1            T   T   F   F   F   F   F   F   F   F   F   F
    5      2            T   T   F   F   F   T   T   F   F   F   F   F
    11     3            T   T   F   F   F   T   T   F   F   F   F   T 
    5      4            T   T   F   F   F   T   T   F   F   F   T   T    

        initialize element 0 with False
        initialize capacity 0 with True

        if weight > capacity:
            answer =  value of index-1 at same capacity
        else:
            answer  = dp[index-1][capacity - weight] or value of index-1 at same capacity

        '''
        summation = sum(nums)
        if summation % 2 != 0: #odd
            return False

        target_sum = summation // 2
        dp = [[False for _ in range(target_sum+1)] for _ in range(len(nums)+1)]

        for row in range(len(nums)+1):
            dp[row][0] = True

        for index, weight in enumerate(nums):
            element_counter = index + 1
            for capacity in range(target_sum+1):
                skip = dp[element_counter-1][capacity]
                take = False #default value

                if weight <= capacity:
                    take = dp[element_counter-1][capacity-weight]
                
                dp[element_counter][capacity] = take or skip

        return dp[len(nums)][target_sum]



        
        