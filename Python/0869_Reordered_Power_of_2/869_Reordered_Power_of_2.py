class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = list(str(n))
        s.sort()

        pow = []
        i = 0

        while len(pow) <= len(s):
            pow = list(str(2**i))
            pow.sort()
            if(pow == s):
                return True
            i += 1
        else:
            return False