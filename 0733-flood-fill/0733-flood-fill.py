class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''

        original = deque((sr,sc))
        starting_value_color = ...

        directions = [(0, 1), (0, -1)...]

        for dir in directions:
            new_r, nc=  dir_x, dir_y
            check if within bound

            if new element matches starting_value_color:
                change its value to source

            new_r, nc append these to the deque

        o(r*c)
        o(r*c)

        '''
  

        color_of_source = image[sr][sc]
        deque = collections.deque([(sr,sc)])
        directions = [(0,1), (0, -1), (-1, 0), (1, 0)]
        ROWS, COLS = len(image), len(image[0])
        visit = set()

        def within_bound(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS:
                return False
            
            return True

        while deque:

            for i in range(len(deque)):
                r, c = deque.popleft()

                if image[r][c] != color_of_source: #0 != 0
                    continue


                image[r][c] = color
                visit.add((r, c))

                for d_r, d_c in directions:
                    new_r, new_c = r + d_r, c + d_c

                    if within_bound(new_r, new_c) and (new_r, new_c) not in visit:
                        deque.append((new_r, new_c))

        return image




                