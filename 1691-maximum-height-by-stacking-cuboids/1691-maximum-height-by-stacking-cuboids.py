class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        '''
        goal:
            MAX HEIGHT of stack
        constraint:
            allowed to skip elements
            [w,l,h] <= [wi,li,hi]

        rearrange dimensions mean? swap height width length if needed

        [[50,45,20],[95,37,53],[45,23,12]]

        [12,23,45],[20,45,50],[37,53,95]
       
        approach:
            formula = 
            (current_pair[0]>=last[0] and current_pair[1] >= last[1] OR
            current[1] >= last[0] and current[0] > last[1])

        [
            [17, 23, 33], [11, 39, 52], [9, 50, 57], [29, 36, 59], [48, 57, 61], [8, 16, 63], [30, 41, 70], [30, 30, 75], [15, 44, 79], [43, 49, 86], 
            [12, 85, 86], [18, 27, 89], [17, 69, 92], [15, 36, 92], [24, 78, 94], [81, 83, 94], [12, 13, 97], [10, 19, 97], [6, 69, 98], [13, 75, 98]
        ]

        [33, 52, 57, 92, 153, 63, 162, 138, 142, 248, 149, 152, 234, 155, 328, 422, 97, 160, 98, 258]
        '''

        for cub in cuboids:
            cub.sort()

   
        cuboids.sort(key=lambda x : (x[0], x[1]))
        print(cuboids)
        res = 0
        dp = [0] * len(cuboids)
        for index, current in enumerate(cuboids):
            w, l, h = current
            dp[index] = h
            for j in range(index):
                old_w, old_l, old_h = cuboids[j]
               

                if w >= old_w and l >= old_l and h >= old_h:
                    dp[index] = max(dp[index],dp[j]+h)
                
            res = max(dp[index], res)

        

        return res




        
        