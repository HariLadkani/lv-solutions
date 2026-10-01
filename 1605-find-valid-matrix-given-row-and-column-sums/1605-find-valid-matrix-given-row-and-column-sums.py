class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        ''' 
        sum to matrix map

        [0,0,0], colSum = [0,0,0]
           
        col_carry = 3
        5 0 0
        3 4 0
        0 2 8 

        '''
        ROWS, COLS = len(rowSum), len(colSum)
        matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                min_value = min(rowSum[row], colSum[col])
                matrix[row][col] = min_value
                rowSum[row] -= min_value
                colSum[col] -= min_value

        return matrix
