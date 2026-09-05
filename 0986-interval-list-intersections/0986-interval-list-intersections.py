class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        '''
        disjoint intervals mean left of next set greater than right of current
        sorted order for intervals

        [0,2],[5,10],[13,23],[24,25]
                               l
        [1,5],[8,12],[15,24],[25,26]
                                r
        [1,2] [5,5] [8, 10] [15, 23]

        goal:
            return intersection
            empty if no intersection

        two problems:
            how to determine overlap
                determine nonoverlap by if smaller's end < larger's start
                move pointer for one with smaller end
                
            how to figure out intersection
                left = max(left of first, left of second)
                right = min(right of first, right of second)

        '''

        result  = []
        i, j = 0, 0

        while i < len(firstList) and j< len(secondList):
            first_start = firstList[i][0]
            first_end = firstList[i][1]

            second_start = secondList[j][0]
            second_end = secondList[j][1]

            
            if not(first_end < second_start or second_end < first_start): #overlap
                new_first = max(first_start, second_start)
                new_second = min(first_end, second_end)
                result.append([new_first, new_second])

            if second_end >= first_end: #second finishes later than first so move first
                i += 1

            else:
                j += 1
                
        return result