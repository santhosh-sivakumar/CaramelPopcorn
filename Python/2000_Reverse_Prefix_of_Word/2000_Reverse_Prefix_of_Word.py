class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        OUT = ''

        try:
            index = word.index(ch) + 1
        except:
            index = 0

        for i in range(0, index):
            OUT += word[i]
        
        OUT = OUT[::-1]
        OUT += word[index:]

        return OUT