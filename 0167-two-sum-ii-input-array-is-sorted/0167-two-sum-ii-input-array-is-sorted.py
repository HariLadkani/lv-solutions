class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''

        constraint:
            same element cannot be reused

            smallest index is 1

        [2,2,2]

        '''
        left, right = 0, len(numbers)-1

        while left < right:
            summation = numbers[left] + numbers[right]

            if summation == target:
                return [left+1, right+1]

            elif summation < target:
                left += 1

            else:
                right -= 1

        