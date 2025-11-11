class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lis_counts = defaultdict(int)
        '''
        goal:
            number of longest increasing subsequences

        constraint: sequence is strictly increasing

        [1, 3, 5, 4, 7]
            3:2 3:1 2:1 1:1

        [2, 2, 2, 2, 2]
         1:1  1:1   1:1   1:1  1:1 0
        
        approach:
            iterate from right side
            for each index, iterate towards index+1 to right
            maintain a tuple in another array to keep track of (length, freq)
            as you iterate to right, maintain a hashmap to find length: freq
            find max length and its freq and store at index 

            at the end of all iterations, find max value and its freq and return as answer its freq. if more than one max value, add their freq for answer
            run time: o(n^2) + o(n)
            space: o(n)

        [1, 3, 5, 4, 7]
                     i
        '''

        length = [1] * len(nums)
        count = [1] * len(nums)
        for index in range(len(nums)-1, -1,-1):
            for r in range(index+1, len(nums)):
                if nums[r] > nums[index]:
                    if 1 + length[r] > length[index]:
                        length[index] = 1 + length[r]
                        count[index] = count[r]
                    elif 1 + length[r] == length[index]:
                        count[index] += count[r]

        max_length = max(length)
        res = 0
        for i in range(len(count)):
            if length[i] == max_length:
                res += count[i]

        return res

                    



        
        

        