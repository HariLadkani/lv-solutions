class Solution:
    def checkValidString(self, s: str) -> bool:
        '''

        [(]  

        [(]

        []

        (***)))(()))
          i
OMax    123
OMin    10-1

        *(

        ""(

        ((

        )(


number of open brakets must be 0



        '''
        open_stack = []

        star_stack = []

        for i, char in enumerate(s):
            if char == '(':
                open_stack.append(i)

            elif char == '*':
                star_stack.append(i)

            else:
                if open_stack:
                    open_stack.pop()

                elif star_stack:
                    star_stack.pop()

                else:
                    return False


        while open_stack:
            if star_stack and open_stack[-1] < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()

            else:
                return False

        return True

        