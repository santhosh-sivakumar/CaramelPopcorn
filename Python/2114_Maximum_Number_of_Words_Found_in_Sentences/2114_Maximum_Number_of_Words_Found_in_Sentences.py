class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        MAX_LEN = 0

        for i in sentences:
            word = i.split()
            if(MAX_LEN < len(word)):
                MAX_LEN = len(word)
            
        return MAX_LEN