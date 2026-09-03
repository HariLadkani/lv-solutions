class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        '''
        [[10,20],[30,200],[30,1000],[30,20]]

           A        A        B        B


           -10     -170     -970      10

        
        - PERSONS need to be split between 2 cities equally

        City A = 1, 2

        City B = 3,4
        '''

        costs.sort(key=lambda x: x[0]-x[1])
        total = 0

        for i in range(len(costs)//2):
            total += costs[i][0]

        for i in range(len(costs)//2, len(costs)):
            total += costs[i][1]

        return total
