class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        [5,-3,5]

              i
         0   1   2  3  4    0   1   2  3  4
         0   1   2  3  4    5   6   7  8  9
        [5, -3, -3, 3, 5, | 5, -3, -3, 3, 5]
                 l
                                    r
currSum = 7
Res = 13

        [5, -3, -3, 3, 5]
                    l
                    r

        left 0
        right 0
        left 0
        currSum 5
        res 5
        ########
        left 0
        right 1
        left 0
        currSum 2
        res 5
        ########
        left 0
        right 2
        left 0
        currSum -1
        res 5
        ########
        left 0
        right 3
        left 3

        [1,2,3,4,5,6,7, -1, -1]
        '''

        total = sum(nums)
        MaxSum = nums[0]
        MinSum = nums[0]
        MaxRes = nums[0]
        MinRes  = nums[0]

        for right in range(1, len(nums)):
            MaxSum = max(nums[right] + MaxSum, nums[right])
            MaxRes = max(MaxSum,  MaxRes)

            MinSum = min(nums[right] + MinSum , nums[right])
            MinRes = min(MinSum, MinRes)
        if MaxRes < 0:
            return MaxRes
            
        return max(MaxRes, total - MinRes)
        




            