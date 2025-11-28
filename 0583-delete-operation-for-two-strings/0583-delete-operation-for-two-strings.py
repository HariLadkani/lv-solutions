class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        input: string word 1 and string word 2
        output: integer minimum operations
        goal:
            min operations to make two words same
            operation is delete of 1 char in either of words 
            same words means same characters with same frequency and order
            empty strings satisfy same condition

        Test case 1:
            word1 = sea
            word2 = eat
            res = 2

        test case 2:
            word1 = "leetcode"
            word2 = "etco"
            res =  4  
            total length of words = 8 + 4 = 12
            LCS = 4 * 2 = 8
            res = 12 - 8 = 4

        test case 3: 
            word1 = ''
            word2 = ''
            LCS = 0
            total = 0
            res = 0

        Questions:
            min size of word1 and word2? 1
            max size of word1 and word2? 500
            if all characters are diff in both words like "afe" vs "lal"? delete all till we get empty strings for both words
        
        Approach:
            FIND longest common subsequence in two words
            return total_length of both words  - longest common subsequence

            Longest common subsequence:
            a b c d
          d 3 3 2 1
          b 3 3 2 1 0
          c 2 2 2 1 0
          d 1 1 1 1  
                
            if two chars do not match:
                max(move i+1 or move j+1)

            if two chars match:
                1 + move both pointers

        run time = o(m*n)
        space = o(m*n)
        '''

        def longest_common_sequence(word1, word2):
            dp = [
                [0 for _ in range(len(word1)+1)] 
                for _ in range(len(word2)+1)
                ] # rows are word 2 and cols are word 1

            for row in range(len(word2)-1, -1, -1):
                for col in range(len(word1)-1, -1, -1):
                    if word1[col] != word2[row]: #if characters do not match
                        dp[row][col] = max(dp[row+1][col], dp[row][col+1])
                    
                    else: #if they match
                        dp[row][col] = 1 + dp[row+1][col+1]

            return dp[0][0]
            
        longest_common_length = longest_common_sequence(word1, word2)
        total_length = len(word1) + len(word2)
        return total_length - 2 *  longest_common_length
  



   
        