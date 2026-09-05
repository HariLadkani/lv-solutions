class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        -2, -1, 0, 0, 1, 2
                           l  
                           r
        -3 + x = target
        x = target - currentSum


        if match found:
            while left <= right:
                loop to skip all duplicates for both left and right

        '''
        result = []
        nums.sort()
        def compute_remaining_twoSum(first_index, second_index, target):
            left, right = second_index + 1, len(nums)-1

            while left < right:
                summation = nums[left] + nums[right]
                if summation == target:
                    result.append([nums[first_index], nums[second_index], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while right > left and nums[right] == nums[right+1]:
                        right -= 1


                elif summation < target:
                    left += 1

                else:
                    right -= 1

        for first_index, first_value in enumerate(nums):
            if first_index > 0 and first_value == nums[first_index-1]:
                continue

            last_second_value  = None
            for second_index in range(first_index+1, len(nums)):
                second_value = nums[second_index]
                if second_value == last_second_value:
                    continue

                compute_remaining_twoSum(first_index, second_index, target - (first_value + second_value))
                last_second_value = second_value
           

        return result


