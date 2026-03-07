class Solution:
    def arraySign(self, nums: List[int]) -> int:
        '''
        RETURN -1, 0, or 1

        -1 * -1 = 1

        even number of neg => positive product
        odd number of neg => neg product
        if any value is 0; return 0 immediatelyg

        '''
        neg_count = 0

        for num in nums:
            if num < 0:
                neg_count += 1
            
            elif num == 0:
                return 0

            
        if neg_count % 2 == 0: #even negatives:
            return 1
        
        return -1
