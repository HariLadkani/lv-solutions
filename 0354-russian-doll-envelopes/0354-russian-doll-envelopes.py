class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''

        goal:
            return max number of envelopes you can put inside the other

        Constraint:
            an envelope has to be less in both width and height to add in another envelope
            CANNOT rotate an envelope

        [5, 4],[6, 4], [6, 7], [2, 3]
        [2, 3], [5, 4], [6, 4], [6, 7]
        l                        r

        edge case:
            if all are equal in width and length:
                return 1

        Approach:
            iterate from right side to left side
            for each index, iterate to index+1 to right side
                if both width and height greater than current:
                    dp[index] = max(dp[index], 1+dp[right])

            return max(dp)

            time = o(n^2)
            space = o(n)

        [[5,4],[6,4],[6,7],[2,3]]
        [2, 3], [5, 4], [6, 4], [6, 7]

        [2, 3], [5, 4], [6, 7], [6, 4]


        '''
        from bisect import bisect_left
        LIS = 1
        envelopes.sort(key=lambda x: [x[0], -x[1]])
        dp = [envelopes[0]]
        heights = [envelopes[0][1]]

        for i in range(1, len(envelopes)):
            if envelopes[i][0] > dp[-1][0] and envelopes[i][1] > dp[-1][1]:
                dp.append(envelopes[i])
                LIS += 1
                heights.append(envelopes[i][1])
                continue

            #width is same
            #height is same or less

            idx = bisect_left(heights, envelopes[i][1])
            dp[idx] = envelopes[i]
            heights[idx] = envelopes[i][1]

        return LIS



            

        

       
            


        return LIS


            
       



        