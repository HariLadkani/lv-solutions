class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        input: array of integers
        output: array of integers
        Goal:
            product of all numbers except itself 
            answer[i] = product of nums[:i] * product of nums[i+1:]


        input: [1, 2, 3, 4]
        output: [24, 12, 8, 6]

        prefix = [1, 1, 2, 6]
        postfix = [24, 12, 4, 1]


        Questions:
            min size of input: 2
            max size of input: 10^5
            can it have neg numbers? yes

        '''
        prefix = [1]
        postfix = [1]
        res = []

        for i in range(1, len(nums)):
            last_num = nums[i-1]
            prefix_value = prefix[-1]
            prefix.append(last_num * prefix_value)

        for i in range(len(nums)-2, -1, -1):
            postfix_value = postfix[-1]
            last_num = nums[i+1]
            postfix.append(last_num * postfix_value)

        postfix = postfix[::-1]
        
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])

        return res
        