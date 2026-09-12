class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        '''
        range: largest - smallest element in subarray
        subarray: contigouos

        goal:
            sum of all subarray (largest-smallest) ranges

        Constraints:
            size of nums: 1 to 1000
            nums[i]: -10^9 to 10^9
            range is always >= 0
            duplicate elements? yes

        edge cases:
            All elements are negative: -100 - -(150)
                                        50
            all elements post: 150 - 100 = 50
            some pos and some neg : 150 - (-50)
                                : 200

            all elements same: 100 - 100 = 0

        Case:
            [1, 2, 3]
        right = [1, 1, 1]
        left = [1, 2, 3]
        stack = [3, 2]
        
        decreasing stack for max
        increasing stack for min
        '''

        res = 0
        

        for i in range(len(nums)):
            maximum = nums[i]
            minimum = nums[i]
            for j in range(i+1, len(nums)):
                maximum = max(maximum, nums[j])
                minimum = min(minimum, nums[j])
                res += maximum - minimum

        return res
                

    
        
        