class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        '''
        guarded cell = cell seen by one or more guards

        goal:
            number of not guarded cells that are not guard and wall

        approach:
            create matrix 
            store all guarded cells 
            explore other cells from the guarded cell in 4 direction and mark the visited cells with guarded
            count unguared ones at end

        '''
        def moveRight(start_row, start_col):
            for col in range(start_col+1, COLS):
                if grid[start_row][col] in ('g', 'w'):
                    return

                grid[start_row][col] = 'guarded'

        def moveLeft(start_row, start_col):
            for col in range(start_col-1, -1, -1):
                if grid[start_row][col] in ('g', 'w'):
                    return

                grid[start_row][col] = 'guarded'

        def moveUp(start_row, start_col):
            for row in range(start_row-1, -1, -1):
                if grid[row][col] in ('g', 'w'):
                    return

                grid[row][col] = 'guarded'

        def moveDown(start_row, start_col):
            for row in range(start_row+1, ROWS):
                if grid[row][col] in ('g', 'w'):
                    return

                grid[row][col] = 'guarded'

        ROWS, COLS = m, n
        grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        
        for row, col in guards:
            grid[row][col] = 'g'

        for row, col in walls:
            grid[row][col] = 'w'



        for row, col in guards:
            moveRight(row, col)
            moveLeft(row, col)
            moveUp(row, col)
            moveDown(row, col)


        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    res += 1


        return res
