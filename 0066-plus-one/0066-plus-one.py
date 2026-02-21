class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        [1, 2, 3]
        
        3 + carry = producr new sum
        extract last digit
        extract carry
      1
        99
         1
        100   
        
        0,0,1
        100
        
        '''
        res = []
        carry = 1
        for right in range(len(digits)-1, -1, -1):
            new_sum = digits[right] + carry
            last_digit = new_sum % 10
            carry = new_sum // 10

            res.append(last_digit)

        if carry > 0:
            res.append(carry)

        res.reverse()
        return res
