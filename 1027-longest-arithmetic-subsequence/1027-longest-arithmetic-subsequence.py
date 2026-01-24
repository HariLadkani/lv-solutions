class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        '''
        goal:
            length of longest arthmetic subsequence
        
        diff between any consecutive elements be same

        [9,4,7,2,10, 13]

         map index 2:
         3:2

         map index 4:
        1:2
        6:2
        3:3
        8:2

        map index 5
        4:2
        9:2
        6:2
        11:2
        3:4




        

        start from index = 1
        if not in map:
            map[diff] = 2
        else:
            map[diff] += 1
        res = max(res, map[diff])


         

        '''
        dp = [{} for _ in range(len(nums))]
        res = 0

        for index, num in enumerate(nums):
            for j in range(index):
                diff = num - nums[j]

                map_j = dp[j]
                map_index = dp[index]

                if diff not in map_j:
                    map_index[diff] = 2

                else:
                    if diff not in map_index:
                        map_index[diff] = 2
                    map_index[diff] = max(map_index[diff], map_j[diff] + 1)
                
                res = max(res, map_index[diff])
        return res