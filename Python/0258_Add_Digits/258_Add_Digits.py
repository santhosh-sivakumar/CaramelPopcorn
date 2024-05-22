class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:
            s, n = 0, num
            while n > 0:
                s += (n % 10)
                n //= 10
            num = s
        
        return num