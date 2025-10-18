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
    
        
        def compute_sum(isMin):
            stack = []
            res = 0

            for index, num in enumerate(nums):

                while stack and (num < nums[stack[-1]] if isMin else num > nums[stack[-1]]):
                    i = stack.pop()
                    right = index - i
                    left = i - stack[-1] if stack else i + 1
                    res += left * right * nums[i]
                
                stack.append(index)

            for i in range(len(stack)):
                left = (stack[i] - (stack[i-1])) if i > 0 else stack[i] + 1
                right = len(nums) - stack[i]
                res += left * right * nums[stack[i]]

            return res

        return compute_sum(False) - compute_sum(True)  

        