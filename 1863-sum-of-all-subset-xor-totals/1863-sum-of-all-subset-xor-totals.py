class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        '''
        xor = ^

        start with 0 as (x xor 0) = x

     0   [1,2,3,,4,4,4,4,4,4]
            1
         0
           i

    
        '''

        res = 0

        def backtrack(index, curr_sum):
            nonlocal res


            if index == len(nums):
            
                res += curr_sum
                return

            for i in range(index, len(nums)):
                backtrack(i + 1, curr_sum ^ nums[i])

           


            res += curr_sum

        backtrack(0, 0)
        return res

        