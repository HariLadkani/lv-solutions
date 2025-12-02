class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        input: 2d matrix with strings in it
        output: integer area of largest square
        goal:
            find largest square with all 1s
            find its area
            if no such square matrix? return 0

        constraints:
            matrix only has 0 or 1

        Questions:
            min size of matrix? 1
            max size of matrix? 300
            what is square? width == height? yes
        
        Notes:
            right, down, diagonal all must be 1
            if current element == 0:
                store 0 at row and col
                continue
            
            current element  = 1 + min(right, down, left)

        run time: 
            m*n
        space: m * n
            
        1 1 1
        1 1 1
        1 1 1

        
        3 2 1
        2 2 1
        1 1 1
        '''

        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]
        biggest_square = 0
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS-1, -1, -1):
                if matrix[row][col] == "0":
                    continue
              
                right, down, diagonal = int(dp[row][col+1]), int(dp[row+1][col]), int(dp[row+1][col+1])
                dp[row][col] = 1 + min(right, down, diagonal)
                biggest_square = max(biggest_square, dp[row][col])

        return biggest_square * biggest_square

        








