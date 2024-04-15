class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        tmp = ''
        count = 0

        for i in range(len(s) - 2):
            tmp = set(s[i:i+3])

            if(len(tmp) == 3):
                count += 1
        
        return count