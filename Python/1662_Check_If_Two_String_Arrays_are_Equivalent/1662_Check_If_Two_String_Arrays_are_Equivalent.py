class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ''.join(word1)
        b = ''.join(word2)

        if(a == b):
            return True
        else:
            return False