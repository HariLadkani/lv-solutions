class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res_left, res_right = None, None
        matches = 0
        map_t = defaultdict(int)
        map_s = defaultdict(int)

        for char in t:
            map_t[char] += 1

        left = 0
        res_len = float("inf")
 
        for r in range(len(s)):
            char = s[r]
      
            map_s[char] += 1

            if char in map_t and map_s[char] == map_t[char]:
                matches += 1

     

            while matches == len(map_t):
                if res_len>r-left+1:
                    res_left, res_right = left, r
                    res_len = r - left + 1

                if s[left] in map_t and map_t[s[left]] == map_s[s[left]]:
                    matches -= 1

                map_s[s[left]] -= 1

                left += 1
       

        




        if res_len == float('inf'):
            return ""
        
        return s[res_left:res_right+1]
