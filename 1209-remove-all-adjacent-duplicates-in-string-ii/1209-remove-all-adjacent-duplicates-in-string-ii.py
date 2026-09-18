class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        removing k adjacent and equal letters and concat remaining together

        goal:
            return final string

        "deeedbbcccbdaa", k = 3
          ---   ---
        "dddaa"

        pbbcggttciiippooaais

        (p,1), (b, 1), (b, 2) (c,1) (g, 1) (g, 2) (t, 1)

        deeedbbcccbdaa
        
        if last value in stack == current:
            pop last value and increment its freq by 1 
            if freq new == k:
                do not add back to stack
            else:
                add to stack


        else:
            add this value with new freq
        
        2 <= k <= 104

        k = 10^4
        axxxxxxxxxxxxxx10^3 x


        "deeedbbcccbdaa"
        char d
        stack []
        stack [('d', 1)]
        @#######
        char e
        stack [('d', 1)]
        stack [('d', 1), ('e', 1)]
        @#######
        char e
        stack [('d', 1), ('e', 1)]
        new_freq 2
        stack [('d', 1), ('e', 2)]
        @#######
        char e
        stack [('d', 1), ('e', 2)]
        new_freq 3
        stack [('d', 1)]
        @#######
        char d
        stack [('d', 1)]
        new_freq 2
        stack [('d', 2)]
        @#######
        char b
        stack [('d', 2)]
        stack [('d', 2), ('b', 1)]
        @#######
        char b
        stack [('d', 2), ('b', 1)]
        new_freq 2
        stack [('d', 2), ('b', 2)]
        @#######
        char c
        stack [('d', 2), ('b', 2)]
        stack [('d', 2), ('b', 2), ('c', 1)]
        @#######
        char c
        stack [('d', 2), ('b', 2), ('c', 1)]
        new_freq 2
        stack [('d', 2), ('b', 2), ('c', 2)]
        @#######
        char c
        stack [('d', 2), ('b', 2), ('c', 2)]
        new_freq 3
        stack [('d', 2), ('b', 2)]
        @#######
        char b
        stack [('d', 2), ('b', 2)]
        new_freq 3
        stack [('d', 2)]
        @#######
        char d
        stack [('d', 2)]
        new_freq 3
        stack []
        @#######
        char a
        stack []
        stack [('a', 1)]
        @#######
        char a
        stack [('a', 1)]
        new_freq 2
        stack [('a', 2)]
        @#######
        '''
        stack = []

        for char in s:

            if stack and char == stack[-1][0]:
                value, freq = stack.pop()
                new_freq = freq + 1

      

                if new_freq != k:
                    stack.append((char, new_freq))

                


            else:
                stack.append((char, 1))

         
        res = ""
        for element in stack:
            res += element[0] * element[1]

        return res