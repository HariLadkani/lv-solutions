class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Input: board with X and o
        Ouput: board with some values  of x changed to o
        Goal:
            capture a surrounded region
            replace all 0s in a region with x

        constraints:
            cell connected HORIzontally and vertically
            region: comprises of connected o cells
            surrounded: 
                region surrounded by x cells
                Not surrounded boundaries of board

            key size constraint: 200 * 200 = 4 * 10^4


        input:
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]

        output:
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]


        input:
        ["X","O","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]

        OUTPUT:
        ["X","O","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]

        
        Question:
            min size of row len and col len? 1 
            max size of row len and col len? 200
            can a board contain anything other than X or 0? No
            can a board not have a single surrounded region?
            
        Approach:
            iterate over all boundaries
            if O: run a dfs on it and mark all connected Os as visited by
                replacing Os with P
            else: continue

            at end of loop:
                mark all Os with X and P with O

            run time: o(m*n)
            space: o(1)
        """
        def dfs(row, col):
            if row == ROWS or col == COLS or row < 0 or col < 0 or board[row][col] == "X":
                return

            board[row][col] = "P"
            dfs(row+1, col) #down movement
            dfs(row-1, col) #up
            dfs(row, col+1) #right
            dfs(row, col-1) #left

        ROWS, COLS = len(board), len(board[0])
    
        for col in range(COLS): #oth row
            if board[0][col] == "O":
                dfs(0, col)

            if board[ROWS-1][col] == "O": #last row
                dfs(ROWS-1, col)

        for row in range(ROWS): #first col
            if board[row][0] == "O":
                dfs(row,0)

            if board[row][COLS-1] == "O": #LAST COLUMN
                dfs(row, COLS-1)


        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "P":
                    board[row][col] = "O"
                
                elif board[row][col] == "O":
                    board[row][col] = "X"

                    


        


        

        