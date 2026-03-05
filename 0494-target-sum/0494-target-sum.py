class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        input = nums with ints
                target

        goal:
            diff ways we can build expressions that evaluate to target 

        cannot skip any element
        choice: add + or -

        [1, 1,  1,  1,  1] target = 3
        2   
            1   
                0   
                    -1
                        -2
                        0
                    1
                        0
                        2
                2
                    1
                        0
                        2
                    3
                        2
                        4
            3
        4       2
                    1
                        0
                        2
                    3
                        2
                        4
                4
                    3
                        2
                        4
                    5
                        4
                        6
            3
                2
                    1
                        0
                        2
                    3
                        2
                        4
                4
                    3
                        2
                        4
                    5

            5
                4
                    3
                    5
                6
                    5
                    7



            1   2   3
        1
        2
        3
        4
        5

        '''
        dp  = {}
        def recursive(index, current_sum):
            if index == len(nums):
                if current_sum == target:
                    return 1
                return 0

            if (index, current_sum) in dp:
                return dp[(index, current_sum)]
                
            sum1 = current_sum + nums[index]
            sum2 = current_sum - nums[index]

            number_ways_with_add = recursive(index+1, sum1)
            number_ways_with_sub = recursive(index+1, sum2)

            ans = number_ways_with_add + number_ways_with_sub
            dp[(index, current_sum)] = ans
            return ans
        return recursive(0, 0)
