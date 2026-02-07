class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False

        letters_found = set()
        for char in sentence:
            letters_found.add(char)

        return len(letters_found) == 26
        