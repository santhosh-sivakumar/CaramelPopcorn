class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mKey = ''.join( key.split(' ') )
        sub = {}
        alpha = 97

        for i in mKey:
            if i not in sub:
                sub[i] = chr(alpha)
                alpha += 1

        OUT = ''
        for i in message:
            if i == ' ':
                OUT += i
            else:
                OUT += sub[i]
                
        return OUT