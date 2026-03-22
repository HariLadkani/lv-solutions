class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        '''
        91/3 = 30 and rem=1 
        
        1, 3, 9, 27, 81 = 91


        12 - 3 = 9
        9 -3 = 6
        6 - 3 = 3
        3 -3 = 0  
        4  

        
        21 - 3 = 18
        18 - 3 = 15
        15 - 3 = 12

        4 + 3 = 7

        91 - 3 = 87
        ......

        1 = 

        30

        21/3 = 7
        6/3 = 2
        2/3

        12/3 = 4
        3/3 = 0

        90
        90/3 = 30
        30/3 = 10


        1
        

        '''
        res = False

     

        def dfs(index, curr_sum):
            nonlocal res
           
            if curr_sum == n:
                res = True
                return

            if curr_sum > n or res==True or 3**index > n:
                return False
            #skip
            dfs(index+1, curr_sum)
            #take it
            dfs(index+1, curr_sum + 3**index)
        dfs(0, 0)
        return res
        