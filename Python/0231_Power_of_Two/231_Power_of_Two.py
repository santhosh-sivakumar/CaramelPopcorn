class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pow = 0
        i = 0
        while (pow <= n):
            pow = 2**i
            i += 1
            if(pow == n):
                return True
        
        return False