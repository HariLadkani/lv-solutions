class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        '''
        target spot must have '0' after jump

        jump allowed between min and max jump number but within bounds of array.

        goal is to reach end index

        edge case:
            end index has '1'

        approach:
            skip with value '1'

            f
        001010
          i

        farthest = 
        

        010010
        012345
        i

        012345
        011010

        01101110
         i
         l
           r

        "0100110"
         0123456
           s
             e

        q deque([0])


        '''

        q = deque([0]) #index
        last_processed = 0

        while q:

            
            index = q.popleft()

            if s[index] == '1':
                continue

            if s[index] == '0' and index == len(s)-1:
                return True

            start = max(index+minJump, last_processed+1)
            end = min(index + maxJump+1, len(s))
        
            for i in range(start, end):
                q.append(i)

            last_processed = end-1
        

        return False

                

