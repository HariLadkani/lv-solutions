class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        'abcde'
            i
        'ace'
          j

            res  112...3

            observations:
                if char equal: 
                        current = dp[index-1][j-1] + 1
                if char not equal:
                        move first word
                        move second word
                        move both

                a b c d e
            a   1 1 1 1 1
            c   1 1 2 2 2
            e   1 1 2 2 3         
        '''
        t1 = len(text1)
        t2 = len(text2)

        dp = [[0 for _ in range(t1+1)] for _ in range(t2+1)]

        for i in range(t2):
            for j in range(t1):
                if text1[j] == text2[i]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[t2-1][t1-1]

        