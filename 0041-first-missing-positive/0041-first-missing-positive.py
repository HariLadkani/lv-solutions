class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''

        [1, 2, 0]
        replace neg with len(nums)+1

        [-3, 4, -5 , -1]
        default return len(nums)


        '''
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums)+1


        for num in nums:
            if abs(num) <= len(nums):
                index = abs(num) - 1
                nums[index] = -abs(nums[index])

        for index, num in enumerate(nums):
            if num >= 0:
                return index + 1
        print(nums)
        return len(nums) + 1