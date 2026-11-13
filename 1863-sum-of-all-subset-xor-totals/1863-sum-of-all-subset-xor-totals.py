class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        '''
        xor = ^

        start with 0 as (x xor 0) = x

        '''

        res = 0
        def backtrack(index, curr_sum):
            nonlocal res
            if index == len(nums):
                res += curr_sum
                return

            new_sum = curr_sum ^ nums[index]
            backtrack(index + 1, new_sum)
            backtrack(index+1, curr_sum)


        backtrack(0, 0)

        return res

        