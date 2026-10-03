class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        '''
        every string in words2 array must be subset of answer in words1

        ["ccbc"] ["ccc", "cb"]

        create an array with 26 letters and add count for minimum needed for each letter to satisfy subset rule
        counts are computed per element
        '''
        words2_map = {}
        res = []
        for word in words2:
            freq_map = Counter(word)
            for key, value in freq_map.items():
                words2_map[key] = max(words2_map.get(key, 0), value)


        for word in words1:
            add_current_word = True
            freq_map_word1 = Counter(word)
            for key, value in words2_map.items():
                if key not in freq_map_word1 or value > freq_map_word1[key]:
                    add_current_word = False
                    break

            if add_current_word:
                res.append(word)


        return res
