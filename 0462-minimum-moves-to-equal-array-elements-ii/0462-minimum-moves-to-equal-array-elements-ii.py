class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        '''
        1, 2, 9, 10

        '''
        nums.sort()

        if len(nums) % 2 == 0: #even
            index1 = len(nums) // 2 - 1
            index2 = len(nums) // 2
            median = (nums[index1] + nums[index2]) // 2

        else:
            median = nums[len(nums) // 2]
        
        res = 0
        for num in nums:
            res += abs(num-median)
        
        return res
        