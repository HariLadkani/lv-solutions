class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        '''
        Input: string array boxes where element is either 0 or 1
        Output: integer array where integer is number of operations
        
        '0':empty
        1: 1 ball
        Goal:
            min operations needed to move all balls to ith box
            
        constraints:
            1 operation = transfer 1 ball from box to adjacent box
            
        Questions:
        in what direction do we move ball left or right? move in both direction
        

        property: number of operations for all balls to right and left side
        
        Approach:
            iterate for each index
                move to left 
                move to right
                in each direction, add right index - i = operations. 
                add these operations if value is 1 else do not add
            
        
        '''
        res = [0] * len(boxes)
        for i in range(len(boxes)):
            left = i-1
            count_left = 0
            right = i + 1
            count_right = 0
            
            while left > -1:
                if boxes[left] == '1':
                    count_left += (i - left)
                left -= 1
                
            while right < len(boxes):
                if boxes[right] == '1':
                    count_right += (right-i) 
                    
                right += 1
                
            res[i] = count_right + count_left
            
        return res
                
        