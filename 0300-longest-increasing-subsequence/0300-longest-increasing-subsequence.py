class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        goal:
            length of LONGEST increasing subsequence

        Input type: integer array
        size of input array: 1 to 2500
        subsequence: non contigious 
        elements: negative and positive

        Test Cases:
        input = [10, 9, 2, 5, 3, 7, 101, 18] 
                 i
        output = 4
        because: [2, 3, 7, 101]

        edge case: [1]
        output: 1

        Approach:
            try stack monotonic
            pop if new element < stack[-1]
            if new element == stack[-1]: ignore new element
            
            [0, 1, 0, 3, 2, 3]
                      
            output = [0, 1, 2,3]

            Brute Force:
            pick and not pick every element in recursion
            for each sequence, check length and return max lenght
            so you made 2 choices at each recursive call
            run time = O(2^n)

            Approach:
                Pick and not pick in recursive solution
                if next element greater, pick it do 1 + max(next greater element count stored in map)
                run time:o(n)
                space: o(n)


        cache = defaultdict(int)
        def increasing_sequence(prev_index, index):
            if index == len(nums):
                return 0

            if (prev_index, index) in cache:
                return cache[(prev_index, index)]

      
            count = increasing_sequence(prev_index, index+1)

            if prev_index == -1 or nums[index] > nums[prev_index]:
                count = max(count, 1 + increasing_sequence(index, index+1))

            cache[(prev_index, index)] = count
            return cache[(prev_index, index)]
            
        [2, 5, 3, 7, 101, 18]
                  2   1    1
            
        return increasing_sequence(-1, 0)

        [10, 9, 2,5,3,7,101,18]
         l                  r
         
        '''
        from bisect import bisect_left
        dp = [nums[0]]
        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

            

        return LIS
        
        
     
        


        