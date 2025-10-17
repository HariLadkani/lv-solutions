class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        '''
        1950: +1
        1960: +1
        1961: -1
        1971: -1

        '''
        sweep_map = {}
        for start, end in logs:
            sweep_map[start] = sweep_map.get(start, 0) + 1
            sweep_map[end] =  sweep_map.get(end, 0) - 1

        curr_population = 0
        max_population = float("-inf")
        res = None

        for year, population in sorted(sweep_map.items()):
            curr_population += population

            if curr_population > max_population:
                res = year
                max_population = curr_population

        return res
