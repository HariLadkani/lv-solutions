class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        '''
        city with most connections will get higher importances
        city with least connections gets lower importants
        importance always increases by 1 starting at 1 and ending at n

        0:2
        1:3
        2:4
        3:2
        4:1

        [2,3,4,2,1]

        [1,2,2,3,4]

        sort on freq and assign citities starting from 1 and increment everytime by 1

        freq * assigned value

        1*1 + 2*2 + 2*3 + 3*4 + 4*5 = 1+4+6+12+20 = 43


        '''

        freq_arr  = [0] * n

        for city1, city2 in roads:
            freq_arr[city1] += 1
            freq_arr[city2] += 1

        freq_arr.sort()
        curr_city_value = 1
        total = 0
        for freq in freq_arr:
            total += curr_city_value * freq
            curr_city_value += 1

        return total