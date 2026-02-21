class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        IV = 4 => V - I = 5 - 1 = 4
        IX = 9 => 10 - 1 = 9
        XL = 40
        XC = 90
        CD = 400
        CM = 900

       

        M C M X C I V
            i
        1000 + 900

        '''
        roman_map = {
            "I":             1,
            "V":             5,
            "X":             10,
            "L":             50,
            "C":             100,
            "D":             500,
            "M":             1000
        }

        total = 0

        for i in range(len(s)):
            if (i-1 > -1) and roman_map[s[i]] > roman_map[s[i-1]]: #todo for index checks
                total -= roman_map[s[i-1]]
                total += roman_map[s[i]] - roman_map[s[i-1]]

            else: #last value was greater than current
                total += roman_map[s[i]]
        return total




