class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''



        '''
        member = set(nums)

        res = 0
        for num in nums:
            count = 0
            if num in member and (num - 1) not in member:
                while num in member:
                    count += 1
                    member.remove(num)
                    num = num + 1
                    res = max(res, count)
                    
        return res
        