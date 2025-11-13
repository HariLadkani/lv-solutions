class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        min and max length of text1 and text2? 1 to 1000
        does it contain only strs? yes

        output can be 0?  yes
        max output: min(text1 len, text2 len)

        brute force: generate sequences and find their match in another text2
        run time = 2^n * m

        Optimized:
            dynamic programing
            if characters match: 
                    return (add 1 and find for rest of string longest common)
            else:
                return max(skip text1 or skip text2 index)

            cache[(index1, index2)] = longest 
        '''
        cache  = {}
        def dfs(index1, index2):
            if index1 == len(text1) or index2 == len(text2):
                return 0

            if (index1, index2) in cache:
                return cache[(index1, index2)]
            length = 0
            if text1[index1] == text2[index2]:
                length += 1 + dfs(index1+1, index2+1)

            else:
                length = max(
                    dfs(index1, index2+1),#move in text2
                    dfs(index1+1, index2)) #move in text1
            cache[(index1, index2)] = length
            return length

        return dfs(0, 0)
