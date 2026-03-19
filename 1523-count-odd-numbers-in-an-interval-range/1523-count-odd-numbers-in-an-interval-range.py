class Solution:
    def countOdds(self, low: int, high: int) -> int:
        '''
        
        3 -> 7

        3, 4, 5, 6, 7

        1 2 3 4 5 6 7 8 9 10
        11 12 13 14 15 16 17 18 19 20

        if start is even:
            (10 - 8) // 2
        if odd:
            (end - start) + 1


        13 17
        13 14 15 16 17 18 19
        
        4//2 = 2

        '''

        difference  = high - low

        if low % 2 == 0:
            if high % 2 == 0:
                return difference // 2
            else:
                return difference // 2 + 1
        else: #odd
            if 
            return difference // 2 + 1