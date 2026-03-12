class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        '''
        
        while friends alive > 2:
            run algo


        if k=1, it removes itself and moves starting to k+1

        0 0 3 4 5
                  i
                  
        steps = 1
        k = 1
        '''
        friends  = [i+1 for i in range(n)]

        friends_killed = 0
        starting_index = 0 #starting index
        while friends_killed != n - 1:
            new_index = (starting_index) % n
            steps = 0
            while friends[new_index] == 0 or steps < k-1 : #1<1
                if friends[new_index] != 0:
                    steps += 1
                new_index += 1
                new_index = new_index % n

            friends[new_index] = 0
            friends_killed += 1

            #in case last friend is left, go to that friend
            starting_index = (new_index + 1) % n
            while friends[starting_index] == 0:
                starting_index += 1
                starting_index = starting_index % n

        return starting_index + 1

        



