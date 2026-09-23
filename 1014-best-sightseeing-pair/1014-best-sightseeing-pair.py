class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        '''

        score = values[i] + values[j] - distance
        distance = index j - index i

        goal:
            max score of a pair
            to maximize:
                values must be higher and closer to each other in array

        [8, 1, 5, 2, 6]
         0  1  2  3  4
         i  
               j
        14 - 4= 10

        [10,1,1,1,1,1,1,1,,1,1,1,1,1,1,1,1,1,1,5,5]
         fails because array is not sorted

        [(1, 1),(2,3),(5,2),(6,4),(8,0)]
                        L
                                    R

        [1,1,1,1,1,1,1,1,1,1,1,5,5,10]
                                 L 
                                    R

        THIS APPROACH fails


        [8,1,100,2,6]
              r
max_value=7
max_value = 6 
max_value = 5

value
dist from value


        '''
        max_from_previous_values = values[0] - 1
        res = float('-inf')
        for r in range(1, len(values)):
            res = max(res, values[r]+max_from_previous_values)
            max_from_previous_values = max(max_from_previous_values-1, values[r]-1)

        return res
