class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''

        a, b = 0 to (sqrt(c))

        0, 1, 2
           l  r

        0**2 + 2**2 = 4 < 5
        1**2 + 2**2 = 5 return true

        left = 0
        right = 2

        left ** 2 + right**2

        if less:
            left += 1
        else:
            right = right - 1

        a + b = sqrt(c)

        10^2 + 10^2 = 200


        0, 1, 2, 3
        l
                 r
        '''

        left = 0
        right = int(math.sqrt(c))

        while left <= right:
            summation = left ** 2 + right ** 2

            if summation == c:
                return True
            elif summation < c:
                left += 1

            else:
                right = right - 1

        return False
