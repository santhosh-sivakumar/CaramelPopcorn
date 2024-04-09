class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        Max = 0
        OUT = ''

        for i in range(len(num) - 2):
            s = num[i: i+3]

            if(s.count(s[0]) == 3):
                if(Max <= int(s)):
                    Max = int(s)
                    OUT = s
        
        return str(OUT)
