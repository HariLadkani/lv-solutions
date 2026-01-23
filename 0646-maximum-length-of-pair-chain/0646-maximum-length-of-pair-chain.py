class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
     
        [a,b] => [c,d]
         p1   <-----   p2
                follows

        goal:
            LENGTH
            longest chain
            can skip pairs(subsequence pattern)

            increasing pairs only form chain
                pair_1[1] < pair_2[0]

       
        [1,2][4,5][5,6][7,8]
         1    2    2    3

        observation:
            LENGTH of longest increasing subsequences of pairs

        Approach:
            sort the input pair
            iterate over all pairs
            maintain dp sequence length array
                check for all previous pairs
                    if previous pair second element < current pair first element:
                            dp[index]  = max(previous_pair + 1, dp[index])

                res = max(res, dp[index])

            return res
        run time: o(n^2)
        space: o(n)
        '''
        pairs.sort()
        dp = [1] * len(pairs)
        res = 0

        for index, [u,v] in enumerate(pairs):
            for j in range(index):
                ju, jv = pairs[j]

                if jv < u:#last element of last pair and first element of current pair
                    dp[index] = max(dp[index],dp[j]+1)
            res = max(res, dp[index])

        return res