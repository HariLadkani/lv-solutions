class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        '''
        1 1 0 0
        0 0 1 0
        0 0 1 0
        0 0 0 1

        0:3
        1:1
        2:0
        3:1

        0: 1
        1:1
        2:2
        3:1


        1 1 1 0
        0 0 1 0
        0 0 0 0
        0 0 0 1

        '''

        rows = defaultdict(int)
        cols = defaultdict(int)

        ROWS, COLS = len(grid), len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    rows[row] += 1
                    cols[col] += 1


        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (rows[row] > 1 or cols[col] > 1):
                    res += 1


        return res 