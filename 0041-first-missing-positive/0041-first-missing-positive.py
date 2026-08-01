class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        [1,2,3,4]

        [-3,4,-5,-1]




        '''

        for i, num in enumerate(nums):
            if num <=0:
                nums[i] = len(nums) + 1

        for i, num in enumerate(nums):
            target_index = abs(num) - 1
            if target_index < len(nums):
                nums[target_index] = - abs(nums[target_index])

        for i, num in enumerate(nums):
            if num > 0:
                return i + 1

        return len(nums) + 1