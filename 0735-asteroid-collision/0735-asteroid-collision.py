class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
      
        6, -2
        6,10, -10

        '''
        stack = []
        

        for a in asteroids:
            ignore = False
            if a > 0:
                stack.append(a)
            #pop and also ignore currrent element
            else:
                while stack and stack[-1] > 0: #collision
                    if abs(a) < abs(stack[-1]):
                        ignore = True
                        break
                    elif abs(a) == abs(stack[-1]):
                        stack.pop()
                        ignore = True
                    else:
                        stack.pop()
                    

                if ignore == False:     
                    stack.append(a)
        return stack


                    

            
