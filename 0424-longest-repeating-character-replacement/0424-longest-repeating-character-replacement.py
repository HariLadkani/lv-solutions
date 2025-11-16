class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        left = 0
        max_len = float('-inf')
      
        #ABABCC
        for i in range(len(s)):
            freq_map[s[i]] += 1
            most_repeated_char_freq = max(freq_map.values())
            other_char_freq = (i - left + 1) - most_repeated_char_freq

            if other_char_freq > k:
                freq_map[s[left]] -= 1
                left += 1

            max_len = max(max_len, i - left + 1)

        return max_len

      
        