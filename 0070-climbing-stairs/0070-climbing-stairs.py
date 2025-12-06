class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        INPUT: integer n
        Output: integer number of ways to reach n
        goal:
            explore diff ways you can reach n steps
            each step: 1 or 2

        1 2 3 4 5 6 
        1 2 3 5 8 13
                              6
                          5(8)   4(5)
                    4(5)        3(3)
                3      2
            2     1  1   0
        1     0  0  0 
      0

        1 2 3 4 5 6 
        1 2 3 5 8 13
        '''
        one_behind, two_behind = 2,1 #start-behind is 3
        if n < 3:
            return n

        for step in range(3, n+1):
            temp = one_behind
            one_behind = one_behind + two_behind
            two_behind = temp

        return one_behind

