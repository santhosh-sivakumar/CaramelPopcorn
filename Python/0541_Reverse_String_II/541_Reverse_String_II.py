class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        if ( k > len(s)):
            return s[::-1]
        
        tmp = OUT = ''
        pos = 0

        for i in range(0, len(s), k):
            tmp = s[i: i+k]
            if (pos % 2 == 0):
                OUT += tmp[::-1]
            else:
                OUT += tmp
            
            tmp = ''
            pos += 1

        return OUT