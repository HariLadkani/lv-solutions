class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        Input: string s and string t
        output: integer number of distinct subsequences 
        goal:
            return number subsequences in s == t
            unique subsequences. one character at an index is not used again 

        questions:
            min size of s and t? 1
            max size of s and t? 1000
            if s.size < t.size? return 0
            are s and t lower case english letters always? yes
        
        s = "rabbbit"
               i
        t = "rabbit"
               j  
        r a b b b i t
        r   3  0 0 0 0 0 0
        a   3 3 0 0 0 0 0     
        b   3 3 3 1 0 0 0
        b   3 3 3 2 1 0 0
        i   1 1 1 1 1 1 0
        t   1 1 1 1 1 1 1 

        COLS - col
        7 - 5 = 2

        

        len parent if < len child: return 0
        if no match: use value of j + 1
        if match: 1 + use value of j + 1
         b  a  b  g  b  a  g
      b [4, 2, 2, 1, 1, 0, 0, 0], 
      a [2, 2, 1, 1, 1, 1, 0, 0], 
      g [1, 1, 1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0, 0, 1]
        '''
        ROWS = len(t)
        COLS = len(s)
        dp = [[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]
        #dp[ROWS][COLS] = 1
        for col in range(COLS+1):
            dp[ROWS][col] = 1

        for row in range(ROWS-1, -1, -1):
            for col in range(COLS-1, -1, -1):
                length_s = COLS - col 
                length_t = ROWS - row
                if (length_s < length_t):
                    continue

                if s[col] == t[row]:
                    dp[row][col] = dp[row+1][col+1] + dp[row][col+1]
                else:
                    dp[row][col] = dp[row][col+1]

        return dp[0][0]





        