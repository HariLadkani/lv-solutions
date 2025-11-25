class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        INPUT: string s
        Output: integer length

        GOAL:
            find length of longest contiguous string in s that has unique characters

        Constraints:
            0<= s.size <=10^5
            s contains english letters, digits, symbols, spaces

        s = "abcabcbb"
        output: 3(abc | abc | bca | cab)

        s = "bbbb"
        output: 1(b)

        Questions?
        min size of s? 0
        max size s? 5 * 10^4
        output minimum? 0
        output maximum? len(s)
        is it only lower case english? english letters, digits, symbols, spaces

        Approach:
                 r
            abcabcbb
               l
        hashset(c, a)
        length = r - l + 1 = 1
        length = 1 - 0 + 1 = 2
        length = 2 - 0 + 1 = 3


        iterate over all s
            while char in set:
                pop left from set
                move left += 1

            add to set current num
            compute length
            max_length = max(current length, max lenth)

        run time: o(n)
        space: o(n) if all s unique
        '''

        max_length = 0
        visited = set()
        left = 0
        for r, char in enumerate(s):
            while char in visited:
                visited.remove(s[left]) #remove chars at left pointer
                left += 1

            visited.add(char)
            curr_length = r - left + 1
            max_length  = max(max_length, curr_length)

        
        return max_length


            


        

        