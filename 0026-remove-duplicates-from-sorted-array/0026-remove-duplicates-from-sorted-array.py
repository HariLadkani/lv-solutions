class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        [1, 2, 3, 4, 3, 4]
                        r
                     w

            
        


        '''
        write_pointer = 0
        prev_write_value = float('-inf')

        for r in range(len(nums)):
            if nums[r] > prev_write_value:
                nums[write_pointer] = nums[r]
                write_pointer += 1
                prev_write_value = nums[r]

        return write_pointer





