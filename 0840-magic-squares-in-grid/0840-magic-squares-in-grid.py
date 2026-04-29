class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        '''

        4 7  15 19
        9 14 15 24
        2 9  15 17

        4  3    8   4 
        13 8    9   13 
        11 15   15  15


        [
            [10,3,5], 
            [1,6,11],
            [7,9,2]
        ]
        '''

        def count_sum_in_rows(row_start, col_start):

            #returns none if fails

            sum_set = set()
            value_set = set()
            for row in range(row_start, row_start+3):
                summation = 0
                for col in range(col_start, col_start+3):
                    summation += grid[row][col]
                    value_set.add(grid[row][col])

                    if grid[row][col] > 9 or grid[row][col] < 1:
                        return None

                sum_set.add(summation)
                
          
            if len(sum_set) == 1 and len(value_set) == 9:
                return sum_set.pop()

        def count_sum_in_cols(row_start, col_start):
            sum_set = set()
            value_set = set()

            for col in range(col_start, col_start+3):
                summation = 0
                for row in range(row_start, row_start+3):
                    summation += grid[row][col]
                    value_set.add(grid[row][col])
                    if grid[row][col] > 9 or grid[row][col] < 1:
                        return None
                sum_set.add(summation)
                

            if (len(sum_set) == 1 and len(value_set) == 9):
                return sum_set.pop()

        def count_diagonals(row, col):
            value_set_right = {
                grid[row][col], grid[row+1][col+1], grid[row+2][col+2]
            }
            right_diag_sum = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]
   
            left_diag_sum = grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col]
            value_set_left = {
                grid[row][col+2], grid[row+1][col+1], grid[row+2][col]
            }
            
            if len(value_set_right) == 3 and len(value_set_left) == 3 and right_diag_sum == left_diag_sum:
                return right_diag_sum

        result  = 0
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(0, ROWS-2):
            for col in range(0, COLS-2):
                sum_rows = count_sum_in_rows(row, col)
                sum_cols = count_sum_in_cols(row, col)
                sum_diag = count_diagonals(row, col)

                if sum_rows and sum_cols and sum_diag and (sum_rows == sum_cols == sum_diag):
                    result += 1

              

        return result


     
        

            
        

           




