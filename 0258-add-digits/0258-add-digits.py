class Solution:
    def addDigits(self, num: int) -> int:
        '''
        input: integer num
        output: integer result
        goal: repeatedly add its digits
            return when only 1 digit left

        test case:
            num = 38
            output 2

        constraint:
            0<=num<=2^32-1

        Questions:
        min value of num? 0 no neg values
        max value of num? 2^32-1


        Approach:
            3 + 8 = 11 < 10 (no)
            1 + 1 = 2 < 10 (yes so stop)

            0 < 10(yes) : stop

            how to retrieve digits?
                38 // 10 = 3
                38 % 10 = 8
                9 % 10 = 0 (stop)
            iterate over added_num till remainder of added_num != 0:
                while remainder(rem) != 0:
                    digit = num // 10
                    rem = num % 10
                    add += digit`
            return add_num
        '''

        res = num 
        while res >= 10: 
            initial_num = res 
            add_num = 0 
            while (initial_num >= 10): 
                digit = initial_num // 10
                add_num += digit
                initial_num = initial_num % 10 
    
            add_num += initial_num  
            res = add_num
        return res

        