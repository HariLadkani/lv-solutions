class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        '''
        nums[i] >= 0
        nums[i] is very very large

        operation:
            - choose pos value and skip value at 0th index
            - nums[i] -= 1
            - nums[i-1] += 1

        goal:
            find max integer after performing operations
            minimize the max int



        [3, 9, 9] 


        [3,7,1,6]

        min = 1 
        max = 7

        1,2,3,4,5,6,7
                l       
                r

        [3,7,1,6]
         3 10 11 17
         4 8

        [3,7,1,6]
        3 10 11 17
        6 12 18  24

        [3,7,1,6]
        3 10 11 17
        5 10 15 20
        '''

        def isValid(target, nums):
            target_sum = 0
            prefix_sum = 0

            for num in nums:
                target_sum += target
                prefix_sum += num

                if prefix_sum > target_sum:
                    return False

            return True


        left, right = min(nums), max(nums)
        res = right

        while left <= right:
            mid = (left + right) // 2

            if isValid(mid, nums):
                res = min(res, mid)
                right = mid - 1

            else:
                left = mid + 1

        return res