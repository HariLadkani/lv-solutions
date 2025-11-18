class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        input: string s and string t
        Output: Boolean 
        Goal:
            find if two strings are anagrams
            anagram:
                same character with same frequency

        Approach:
            build a hashmap of s with char: count
            build a hashmap of t with char: count

            if two maps same: valid anagram
            else: false

        Run time: o(len(s) + len(t))
        space: o(len(s)+len(t))


        Question:
            min size of s and t? 1
            max size of s and t? 5 * 10^4
            does s and t have only lower case char? yes
        
        anagram and nagaram

        a: 3
        n: 1
        g: 1
        r: 1
        m: 1

        n: 1
        a: 3
        g: 1
        r: 1
        m: 1

        '''
        freq_map_s = {}
        freq_map_t = {}

        if len(s) != len(t):
            return False

        for index in range(len(s)):
            char_s = s[index]
            char_t = t[index]
            freq_map_s[char_s]  = freq_map_s.get(char_s, 0) + 1
            freq_map_t[char_t] = freq_map_t.get(char_t, 0) + 1

        return freq_map_s == freq_map_t
        