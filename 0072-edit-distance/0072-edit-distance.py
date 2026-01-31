class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        optimization problem with two strings
        two strings should ring LCS

        word1 = "horse", word2 = "ros"

        h o r s e word1
      0
    r 1 1 2 2 3 4
    o 2 2 1 2 3 4
    s 3 3 2 2 2 3
        hor
        ro

        a b
    a   0 1  
    b   2
    c     

    [    0
        [1, 0, 0, 0, 0, 0], 
        [2, 0, 0, 0, 0, 0], 
        [3, 0, 0, 0, 0, 0]
    ]

        delete = longest common sequence

        observation:   
            if two char same: look at diagonal 
            if not same:
                current = min(
                            delete => 1 + dp[i][j-1], 
                            replace or insert => 1 + dp[i-1][j-1]

                a
            0   1   
        a   1   0
        b   2   

        [0, 1], 
        [1, 0], 
        [2, 0]

        '''
        w1, w2  = len(word1), len(word2)
        dp = [[0 for _ in range(w1+1)] for _ in range(w2+1)]

        for row in range(1, w2+1):
            dp[row][0] = row 
        
        for col in range(1, w1+1):
            dp[0][col] = col
        
        dp[0][0] = 0 # word1="" and word2 = ""
        
        
        for row in range(1, w2+1):
            for col in range(1, w1+1):
                if word1[col-1] == word2[row-1]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    dp[row][col] = 1 + min(
                        dp[row][col-1],
                        dp[row-1][col],
                        dp[row-1][col-1]
                    )

        return dp[w2][w1]
        

