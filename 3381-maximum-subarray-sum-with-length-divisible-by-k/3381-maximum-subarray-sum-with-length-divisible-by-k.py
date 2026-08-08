class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        '''
        [ -1, -2, -3, -4, -5], k = 4
          -1   -3  -6  -10  -15

        res = -10
        0: 0
        1: -15
        2: -3
        3: -6
        4: -10
        
        [-5,1,2,-3,4], k = 2
        -5  -4 -2 -5 -1
        
        res = 3
        0: -4
        1: -5
        

        process:
            res = max(res, sum diff)
            keep minimum running sum at index

        [-1,-2,-3,-4,-5]
        4

        index 0
        num -1
        running sum -1
        hash_map {1: -1}
        res -inf
        end+++++++
        index 1
        num -2
        running sum -3
        hash_map {1: -1, 2: -3}
        res -inf
        end+++++++
        index 2
        num -3
        running sum -6
        hash_map {1: -1, 2: -3, 3: -6}
        res -inf
        end+++++++
        index 3
        num -4
        running sum -10
        hash_map {1: -1, 2: -3, 3: -6, 0: -10}
        res -inf
        end+++++++
        index 4
        num -5
        running sum -15
        hash_map {1: -15, 2: -3, 3: -6, 0: -10}
        res -14
        end+++++++
         
        '''

        hash_map = {0:0} #modulus: min_sum
        res = float("-inf")
        running_sum = 0
        for index, num in enumerate(nums):
  
            running_sum += num
    

            length = index + 1
            if length % k in hash_map:
                res = max(res, running_sum - hash_map[length % k])
                hash_map[length%k] = min(hash_map[length % k], running_sum)
            else:
                hash_map[length%k] = running_sum

       
           
        return res
