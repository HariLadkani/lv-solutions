class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        '''
        arr = [9,4,2,10,7,8,8,1,9]

        
        9, 4, 2, 10, 7, 8, 8, 1, 9
                           r

        currSign= -1
        PreviousSign=None
        currLen=2
        res = 5

        [9,4,2,10,7,8,8,1,9]
                    r
       
        r 4
        current sign -1
        previousSign 1
        maxLen 5
        currLen 5
        ###########
        r 5
        r 6
        current sign 1
        previousSign None
        maxLen 6
        currLen 6
        ###########
        r 7
        current sign -1
        previousSign 1
        maxLen 7
        currLen 7
        ###########




        '''

        currLen = 1
        maxLen = 1
        previousSign = None


        for r in range(len(arr)-1):
         
            
            if arr[r] > arr[r+1]:
                currentSign = 1
            
            elif arr[r] < arr[r+1]:
                currentSign = - 1

            else:
                previousSign = None
                currLen = 1
                continue

   

            if currentSign != previousSign:
                currLen += 1
                previousSign = currentSign

            else:
                currLen = 2 
                previousSign = currentSign

            maxLen = max(maxLen, currLen)

         
        return maxLen

            
            

