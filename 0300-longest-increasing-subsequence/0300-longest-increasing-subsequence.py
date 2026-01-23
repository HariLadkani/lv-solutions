class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        [10,9,2,5,3,7,101,18]
        [1, 1,1,2,2,3,4,4]

        '''
        dp = [1] * len(nums)
        res = 1

        for index in range(len(nums)):
            current_element = nums[index]
            for left in range(index):
                if nums[left] < current_element:
                    dp[index] = max(dp[left] + 1, dp[index])
            res = max(res, dp[index])

        return res

        
        
     
        


        