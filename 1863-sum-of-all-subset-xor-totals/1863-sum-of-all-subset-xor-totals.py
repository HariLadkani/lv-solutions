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

            print(f"ENTER: index={index}, curr_sum={curr_sum}")

            if index == len(nums):
                print(f"  BASE CASE: adding {curr_sum} to res")
                res += curr_sum
                return

            for i in range(index, len(nums)):
                print(f"  CHOOSE: nums[{i}] = {nums[i]}")

                backtrack(i + 1, curr_sum ^ nums[i])

                print(f"  BACKTRACK: returned to index={index}, curr_sum={curr_sum}")


            res += curr_sum

        backtrack(0, 0)
        return res

        