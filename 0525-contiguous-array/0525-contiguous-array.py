class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
              
         +1 for 1
         -1 for 0
        length = index + 1

        [0, 1,  1,  1,  1,  1,  0,  0,  0]
         -1 0   1   2   3   4   3   2   1
        
        -1:0
        0:1
        2:3
        3: 4
        if running sum is 0: res = len(curr_index) + 1
        elif if running sum seen before, compute length diff and do res = max(res, length diff)
        
        do not populate running sum if already present


        '''

        count_to_index = {0:-1}
        res = 0
        running_count = 0
        for index, num in enumerate(nums):
            running_count += (+1 if num == 1 else -1)

            if running_count in count_to_index:
                res = max(res, index - count_to_index[running_count])
            else:
                count_to_index[running_count] = index

        return res
