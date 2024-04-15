class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = [chr(i) for i in range(97, 123)]

        for i in alpha:
            if (i not in sentence):
                return False
        
        return True