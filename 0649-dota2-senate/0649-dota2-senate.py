class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        '''
        input: senate string with R and D

        constraint:
            start from left and go right

        goaL:
            predict out of R and D, which party has senators left and is winner
            party that looses all senators looses

        test hypothesis: most frequent party wins wRONG THIS case proves it is wrong
            RRDDD
        
        RDDRD
        
        RDRD
        RDD

        RDRDD

        R

        RDD
         i
        R:1
        D:1
        D:2

        RDDRD
          I
        r: 1
        d:2

        RDRRD
        012345
        i
        R=> [0, -3, 4]
             i
        D=> [-1,-2, -5]
                j
        '''

        deque_r = deque([])
        deque_d = deque([])

        for index, s in enumerate(senate):
            if s=='R':
                deque_r.append(index)
            else:
                deque_d.append(index)

        while deque_r and deque_d:
            index_r = deque_r.popleft()
            index_d = deque_d.popleft()

            if index_r < index_d:
                deque_r.append(index_r+len(senate))

            else:
                deque_d.append(index_d+len(senate))


        if len(deque_r) == 0:
            return "Dire"

        return "Radiant"
                