class Solution:
    def scoreOfString(self, s: str) -> int:
            OUT = 0

            for i in range(0, len(s) - 1):
                if( ord(s[i]) > ord(s[i+1]) ):
                    OUT += ( ord(s[i]) - ord(s[i+1]) )
                else:
                    OUT += ( ord(s[i+1])  - ord(s[i]))

            return OUT