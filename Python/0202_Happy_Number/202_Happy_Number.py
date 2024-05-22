class Solution:
    def isHappy(self, n: int) -> bool:
        
        OUT = []
        while( n > 1 ):
            sum = 0
            while (n > 0) :
                sum += (n % 10)**2
                n //= 10
            
            if sum in OUT:
                return False
            else:
                OUT.append(sum)
                n = sum

        if n == 1:
            return True
        else:
            return False