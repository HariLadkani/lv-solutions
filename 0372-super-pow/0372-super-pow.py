class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        '''
        a^b mod 1337

        b = [1,0] = b= 10

        2^10 mod
        '''

        b_str = "".join(str(b_element) for b_element in b)
        b = int(b_str)

        res = 1

        while b > 0:
            if b % 2 != 0: #odd
                b -= 1
                res = res * a

            b = b // 2
            a = a * a

        return res % 1337