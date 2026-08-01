class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        freq must match and so are chars for anagram

        group by count using 26 letters of english

        if len(strs) == 0:
            return [[""]]
        
        loop over strs
            loop over char and form a list with counts of each char where first elment in list stores counts of a and last stores counts of z
        '''

        if len(strs) == 0:
            return [[""]]

        res = []
        anagram_map = defaultdict(list)

        for string in strs:
            freq_map = [0] * 26
            for char in string:
                freq_map[ord(char) - ord("a")] += 1

            key = tuple(freq_map)
            anagram_map[key].append(string)


        for value in anagram_map.values():
            res.append(value)

        return res

            