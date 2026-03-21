class Solution:
    def largestOddNumber(self, num: str) -> str:
        '''
        find substring of num
        find largest valued odd int

        goal:
            return "" if no exists

        354238
            i

        move from right to left and if any digit is odd, return start to end


        constrainsts:
            substring is cont

        '''

        num = int(num)

        while num > 0:
            right = num%10

            if right % 2 != 0:
                return str(num)

            num=num//10

        return ""