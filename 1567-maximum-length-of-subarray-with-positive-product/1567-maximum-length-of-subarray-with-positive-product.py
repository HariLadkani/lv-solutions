class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        '''
        input: integer nums
        output: integer max length of subarray with positive product

        goal:
            find subaary with positive product
            find their length and return max length out of all
        
        constraint:
            subarray = contiguous 
            positive product means greater than 0
            if no valid answer, return 0
        
        property:
            we cannot have odd number of negatives
                if we have odd number, remove earliest one negative. 
                This leaves even number of negatives and hence answer started earliest negative + 1 till current 

        [-1,-2,-3, 2, 2]
          1  1  3   
          0  2  2  3
                3       5
        [1,2,2,-1, -1, -1, 1, -1]
earliest        l   
 neg     0 0 0  1   2   3  3   4   
 res     1 2 3  0   5   5  5   8

        [0,1,-2,-3,-4]
neg      0
res      0
        '''

        negative_count = 0
        res = 0
        earliest_negative_index = None
        earliest_index = 0

        for i, num in enumerate(nums):
            if num < 0:
                earliest_negative_index = i if earliest_negative_index is None else earliest_negative_index    
                negative_count += 1

            elif num == 0:
                earliest_negative_index = None
                negative_count = 0
                earliest_index = i + 1

            if negative_count % 2 == 0: # even number of negative values so product is even
                res = max(res, i - earliest_index + 1)

            else: #odd number of negative values so odd product. remove first ever negative value to make even negatives
                res = max(res, i-earliest_negative_index)

        return res

