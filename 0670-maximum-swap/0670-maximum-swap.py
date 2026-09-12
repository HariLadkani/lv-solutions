class Solution:
    def maximumSwap(self, num: int) -> int:
        '''
        swap once or none time

        goal:
            maximize number


        8 8 0 22
            i   
        88202    

        88220
        9973
        
        011

        9 9 7 3
            i
        
        8 8 0 2 2
         (8, 2)   (2, 4) (2,4)  (2, 4)  -inf
        '''
        num_string = list(str(num))
        max_after_current = [(0, 0)] * len(num_string)

        for right in range(len(num_string)-2, -1, -1):
            next_value = int(num_string[right+1])
            max_after_next_value = int(max_after_current[right+1][0])
            max_after_next_value_index = max_after_current[right+1][1]

            if next_value > max_after_next_value:
                max_after_current[right] = (next_value, right+1)
            else:
                max_after_current[right] = (max_after_next_value, max_after_next_value_index)

        for right in range(len(num_string)):
            max_after_current_value, max_after_current_index = max_after_current[right]
            if int(num_string[right]) < int(max_after_current_value):
                num_string[right], num_string[max_after_current_index] = num_string[max_after_current_index], num_string[right]
                break


        return int("".join(num_string))




       

        