class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        elements = [7, 7, 5, 7, 3, 3, 10, 10]
                    ----------           ------
                          ---------- 
                                --------
                                             i
                    7: 3
                    5: 5
                    3: 6
                    10: 8

                    ab | ab | cc

                    freq map:
                    10: 2

                    total length of a block - freq of most freq element =  0
                    7 - 3 = 4


                    



                    [7, 7, 7, 7, 3, 7, 3]
                    [7, 7, 7, 7, 7, 7, 7]
        min cost = 2 + 2 =  4

        goal: max freq matters

        a b a b c c
        -----   ---
          -----
        -------



        '''

        ends = {}

        for index, char in enumerate(s):
            ends[char] = index
        print("ends", ends)
        count = 0
        res = []
        end = 0
        for index, char in enumerate(s):
            count += 1
            
            end = max(ends[char], end)
            print("count", count)
            print("end", end)
            if end == index:
                res.append(count)
                count = 0
                end = 0


        return res
