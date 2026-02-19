class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0

        for sentence in sentences:
            words = sentence.split()
            res = max(res, len(words))
        return res
        