class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        '''
        if dir == 1:
            shift right char in s from start to end
        else:
            shift left from start to end

        cyclic nature of shift

        goal:
            shifted string

        start to end is a range of characters that would be shifted

        run time is issue because it is n^2

        
        '''
        res = []
        prefix_array = [0] * (len(s) + 1)
            
        for char in s:
            res.append(ord(char) - ord("a"))

        for start, end, direction in shifts:
            prefix_array[start] = prefix_array[start] + (1 if direction == 1 else -1)
            prefix_array[end+1] = prefix_array[end+1] + (-1 if direction == 1 else 1)

        shift = 0

        for index, shift_marker in enumerate(prefix_array):
            shift += shift_marker
            prefix_array[index] = shift
        print(res)

        for index, num_char in enumerate(res):
            shift = prefix_array[index]
            num_char =  (num_char+shift) % 26
            char = chr(num_char + ord("a"))
            res[index] = char

        return "".join(res)
          
                    

