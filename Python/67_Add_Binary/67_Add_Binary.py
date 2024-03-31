class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = y = 0
        a = a[::-1]
        b = b[::-1]

        for i in range(len(a)):
            if (a[i] == '1'):
                x += 2**i
        
        for i in range(len(b)):
            if (b[i] == '1'):
                y += 2**i

        print(x, y, x+y)
        
        return str(bin(x+y))[2:]