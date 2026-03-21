class Solution:
    def isUgly(self, n: int) -> bool:
        '''
        ugly number must have only prime factor of 2,3,5

        2 * 2 = 4
        6

        [
            True, =>0 
            True, => 1
            True => 2
            True => 3
            FALSE => 4  
            TRUE, => 5
            fALSE => 6


        ]
        10
        3 * 3 = 9
        4 * 4 = 16

       n = 14
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
       [f,F,T,T,f,T,f,T,f,f,f, T, f, T,  F]
                      

        14/7 = 2

        i*i, n, i

        '''
        if n<0:
            return False

        for p in [2,3,5]:
            while n%p == 0:
                n = n//p

        return n == 1
        