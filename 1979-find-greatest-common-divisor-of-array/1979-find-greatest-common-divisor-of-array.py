class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a,b = max(nums), min(nums)
        #max = a = 8, min = b = 3
        '''
        (8, 3) => 8, 2
        (3, 2) => 3, 3%2 =2, 1
        (2, 1) => 1, 0

        '''
        print("a and b", a, b)
        while b > 0:
            temp = a
            a = b
            b = temp  % b

            print("a and b", a, b)

        return a