class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        '''
        range: res - smallest element in subarray
        subarray: contigouos

        goal:
            sum of all subarray (res-smallest) ranges

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

        (res_i - smallest_i) + (res_b-smallesb) = res_i + res_b - smallest_i - smallest_b

        how many times a particular number appears to be res and how many times it is minimum

        res
        1: 1
        2: 2
        3: 3

        smallest
        1:3
        2:2
        3:1

        1*1+2*2+3*3 = res = 14
        1*3+2*2 + 3 = 10

        first compute number of subarrays each element in nums appears to be res 
            - expand till others are smallest
            maintain a decreasing stack strictly less than
            if property violated, compute (left + 1) * (right+1)
            right = current_index - popped_index - 1
            left = popped_index - (stack[-1] if stack else 0)


        then computer numbert of subarrays for each in nums where nums is smallest

        [1,2,3]
        r 0
        decreasing stack []
        r 1
        decreasing stack [0]
        decreasing stack [0]
        popped_index 0
        right 0
        left 0
        nums 1 appears in 1 subarrays
        r 2
        decreasing stack [1]
        decreasing stack [1]
        popped_index 1
        right 0
        left 1
        nums 2 appears in 2 subarrays
        decreasing stack [2]
        8


        [4,-2,-3,4,1]

        smallest
        4:1
        -2:2
        -3:9
        4:1
        1:2

        largest:
        4: 3
        -2:2
        -3: 1
        4:8
        1:1

        12-4-3+32+1
        6+32 = 32 + 6 = 38
        

        [4,-2,-3,4,1]
                 r
        stack []
        #######
        stack [0]
        #######
        stack [0, 1]
        #######
        stack [0, 1, 2]
        stack [0, 1, 2]
        left 1
        right 0
        -3 exists in 2 subbarays
        stack [0, 1]
        left 1
        right 1
        -2 exists in 4 subbarays
        stack [0]
        left 0
        right 2
        4 exists in 3 subbarays
        #######
        stack [3]
        #######
        stack [3, 4]
        stack [3, 4]
        left 1
        right 0
        1 exists in 2 subbarays
        stack [3]
        left 3
        right 1
        4 exists in 8 subbarays
        32

        39
        21

        '''
        def compute(large_calculation):
            res = 0
            stack = []

            for r in range(len(nums)):
   
                while stack and (nums[stack[-1]] <= nums[r] if large_calculation else nums[stack[-1]] >= nums[r]):
          
                    popped_index = stack.pop()
                    right = (r - 1) - popped_index
                    left = popped_index - (stack[-1] + 1 if stack else 0)
                    res += (left + 1) * (right + 1) * nums[popped_index]
        

                stack.append(r)
   
            
            
            while stack:
                popped_index = stack.pop()
                left = popped_index - (stack[-1] + 1 if stack else 0)
                right = len(nums) - popped_index - 1
                res += nums[popped_index] * (left + 1) * (right + 1)
         
            
           

            return res
        return compute(True) - compute(False)

    
       


        





        

    
        
        