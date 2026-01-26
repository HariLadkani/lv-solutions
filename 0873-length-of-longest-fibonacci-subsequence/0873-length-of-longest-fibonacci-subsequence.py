class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        '''
        input: STRICTLY increasing positive integers
        output: length of longest fib sequence or 0 if not exists
        
        [1,3,7,11,12,14,18]
         1      2

        index map 0
        1:1

        map 1
        3:1
        4:2

        index map 3:
        12:2
        14:2
        18:2
        11:1

        index map 4
        24:3
        28:3

        index map 5

        [1,2,3,4,5,6,7,8]
         
        map 0
        1:1

        map 1
        2:1
        3:2

        map 2
        3:1
        6:3
        4:2

        map 3
        5:2
        6:2
        7:2
        8:3

        map 4
        5:1
        10:3
        6:2
        7:2
        8:4
        9:2
        
        map 5
        12:4

        
        map 5

        Aproach:
        res = 0
        iterate over entire array
            currentmap[currentnumber] = 1
            inner iterate till current index 
                if current value in map_j:
                    add map_j count + 1 and store with new total
                    compute max res too
                store key(current value + value j) = 2


        {}
        {3: 2}
        {4: 2, 5: 2, 6: 3}
        {5: 2, 6: 2, 7: 2, 8: 3}
        {6: 2, 7: 2, 8: 2, 10: 3, 9: 2}
        {7: 2, 8: 2, 9: 2, 12: 4, 10: 2, 11: 2}
        {8: 2, 9: 2, 10: 2, 11: 2, 14: 3, 12: 2, 13: 2}
        {9: 2, 10: 2, 11: 2, 12: 2, 16: 4, 13: 2, 14: 2, 15: 2} 
   
        '''

        res = 0
        dp = [{} for _ in range(len(arr))]

        for index, num in enumerate(arr):
            for j in range(index):
                dp[index][num+arr[j]] = 2
                if num in dp[j]:
                    dp[index][num+arr[j]] = dp[j][num] + 1
                    res = max(res, dp[index][num+arr[j]])

        

        return res