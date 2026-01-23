class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        '''
        [1,3,1]

        
                /
            /       \
        /               \

        [2,1,1,5,6,2,3,1]
         1 1 1 2 3 2 3 1
         2 1 1 3 3 2 2 1   

        total length - increasing length - decreasing sequence length + 1

     

         


                            6
                       5 
                                    3
        2                         2
            1  1                        1

        mountain array: increasing + pivot + decrease
        minimize removals: maximim length of increase + pivot + maximum length of decreasing

        approach:
            find max increasing subsequence length arrays
            find max decreasing length arrays
            iterate with zipped and use formula 
            removals = total length - increasing length - decreasing sequence length + 1
            minimize removals

        '''
        def find_subsequence_dp(nums):
            dp = [1] * len(nums)
            for index,num in enumerate(nums):
                for j in range(index):
                    if num>nums[j]:
                        dp[index] = max(dp[index], 1+dp[j])

            return dp

    

        increasing_dp = find_subsequence_dp(nums)
        decreasing_dp = find_subsequence_dp(nums[::-1])
        decreasing_dp.reverse()

        res = len(nums)
        for l1, l2 in zip(increasing_dp, decreasing_dp):
            if l1 > 1 and l2 > 1:
                res = min(res, len(nums) - l1 -l2 + 1)
            print(f"l1:{l1} and l2:{l2} and res:{res}")

        return res

        