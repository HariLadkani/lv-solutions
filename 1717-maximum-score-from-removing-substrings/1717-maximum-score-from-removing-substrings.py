class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        '''

        "cdbcbbaaabab" x=4 (ab) and y=5 (ba)
        "cdbcbbaaab"
        "cdbcbbaa"
        "cdbcba"
        

        bbaaabab

        

       

        - prioritize removing ba if y > x else ab

        '''

        find_first = "ab"
        find_second = "ba"
        find_first_value = x
        find_second_value = y

        if find_first_value<find_second_value:
            find_first, find_second = find_second, find_first
            find_first_value, find_second_value = find_second_value, find_first_value

        total = 0
        stack = []
        for char in s:
            if stack and (stack[-1] + char) == find_first:
                stack.pop()
                total += find_first_value

            else:
                stack.append(char)

        second_stack = []
        for char in stack:
            if second_stack and (second_stack[-1] + char) == find_second:
                second_stack.pop()
                total += find_second_value

            else:
                second_stack.append(char)


        return total