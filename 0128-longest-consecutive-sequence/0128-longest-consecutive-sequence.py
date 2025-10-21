class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''



        '''
        member = set(nums)

        res = 0
        for num in member:
            count = 0
            if (num - 1) not in member:
                while num in member:
                    count += 1
                    num = num + 1
                    res = max(res, count)
                    
        return res
        