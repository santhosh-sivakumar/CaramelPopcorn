class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        LIST = [str(ord(i) - 96) for i in s]

        OUT = int(''.join(LIST))

        for i in range(k):
            tmp = 0
            while(OUT != 0):
                tmp += OUT % 10
                OUT //= 10
            OUT = tmp
        
        return OUT