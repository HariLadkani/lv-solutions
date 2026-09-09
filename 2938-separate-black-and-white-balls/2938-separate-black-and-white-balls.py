class Solution:
    def minimumSteps(self, s: str) -> int:
        '''
        black = 1
        white = 0

        operation:
            pick two adjacent and swap
            

        goal:
            min steps to move all white balls to left and black to right

        10110


        12    
        101100
          l
             r
        1+3+


        01100110
            l
                 r
        00001111
            l

        2+2+4

        maintain left pointer where left means everything before left has white balls

        maintain right
        loop with right 
            if current is 1: continue
            if current is 0: 
                steps += right - left
                left += 1
        '''


        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] == '1':
                continue

            res += right - left
            left += 1

        return res