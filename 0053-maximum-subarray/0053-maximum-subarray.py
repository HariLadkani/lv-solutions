class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        largest sum = largest right - smallest left

        [-2,1,-3,4,-1,2,1,-5,4]
                 l
                             r
currSum= 5
Res= 6

         loop:
            while current sum is neg and left < right, shrink the window and update current sum

            process current element and update current sum


        -2 -1 -4 0 -1 1 2 -3 1



        if sum is increasing, keep expanding else shrink

        '''

        currSum, res = 0, float("-inf")

        left = 0

        for r in range(len(nums)):
            while currSum < 0 and left < r:
                currSum = currSum - (nums[left])
                left += 1

            currSum += nums[r]
            res = max(res, currSum)

        
        return res