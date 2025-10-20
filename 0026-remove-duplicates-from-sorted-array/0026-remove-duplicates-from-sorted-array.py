class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        [1, 1, 1, 2, 3, 4]
            l     r

        


        '''
        left = 0
        right = 0

        while right < len(nums):
            nums[left] = nums[right]
            while right < len(nums) and nums[right] == nums[left]:
                right += 1

            left += 1
        
        return left