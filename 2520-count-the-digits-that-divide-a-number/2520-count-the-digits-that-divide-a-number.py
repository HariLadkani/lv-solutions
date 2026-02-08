class Solution:
    def countDigits(self, num: int) -> int:
        '''
        121 % 10 = remainder = 1
        121 // 10 = 12
        
        12%10 = 2
        12 / 10 = 1

        1 % 10 = 1
        1 / 10 = 0
        '''
        res = 0
        num_current = num
        while num_current != 0:
            right_most_digit = num_current % 10
            remaining_digits = num_current // 10

            if num % right_most_digit == 0:
                res += 1
            
            num_current = remaining_digits
        
        return res

        