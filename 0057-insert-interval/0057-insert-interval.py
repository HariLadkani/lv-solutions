class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        6 - 8
                9 - 5

        '''

        index = 0
        res = []

        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            res.append(intervals[index])
            index += 1

        while index < len(intervals) and (intervals[index][0] <= newInterval[1]):
            newInterval = [min(newInterval[0], intervals[index][0]), max(newInterval[1], intervals[index][1])]
            index += 1

        res.append(newInterval)

        res += intervals[index:]

        return res







        