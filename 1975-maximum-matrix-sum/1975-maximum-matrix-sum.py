class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ''' 
        goal is to convert as many neg values to positives

        could help to pick least neg value as first and find greatest neighbours
        keep all neg values in a heap and maintain a hashmap to mark positive values

        1   2   3
        -1 -2   3

        '''
        abs_sum = 0
        neg_count = 0
        min_abs_value = float('inf')
        ROWS, COLS = len(matrix), len(matrix[0])

        for row in range(ROWS):
            for col in range(COLS):
                abs_sum += abs(matrix[row][col])
                if matrix[row][col] < 0:
                    neg_count += 1

                min_abs_value = min(min_abs_value, abs(matrix[row][col]))

        if neg_count % 2 != 0: #odd
            abs_sum -= 2*min_abs_value

        return abs_sum
                    