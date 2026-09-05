class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        "babad"

        i 0
        left 0
        right 0
        longest_substring 
        longest_substring_length 1
        left -1
        right 1
        ##############
        i 1
        left 1
        right 1
        longest_substring 
        longest_substring_length 1
        left 0
        right 2
        ##############
        left 0
        right 2
        longest_substring 
        longest_substring_length 3
        left -1
        right 3
        ##############
        i 2
        left 2
        right 2
        longest_substring 
        longest_substring_length 3
        left 1
        right 3
        ##############
        left 1
        right 3
        longest_substring 
        longest_substring_length 3
        left 0
        right 4
        ##############
        i 3
        left 3
        right 3
        longest_substring 
        longest_substring_length 3
        left 2
        right 4
        ##############
        i 4
        left 4
        right 4
        longest_substring 
        longest_substring_length 3
        left 3
        right 5
        ##############

        '''
        longest_substring_length = 0
        longest_substring = ""

        for i in range(len(s)):
            print("i", i)
            left = i 
            right = i

            while left > -1 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > longest_substring_length:
                    longest_substring_length = (right - left + 1)
                    longest_substring = s[left:(right+1)]
        

                left -= 1
                right += 1

            left = i
            right = i + 1

            while left > -1 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > longest_substring_length:
                    longest_substring_length = (right - left + 1)
                    longest_substring = s[left:right+1]

                left -= 1
                right += 1

        return longest_substring

