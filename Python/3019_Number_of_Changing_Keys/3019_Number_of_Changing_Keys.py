class Solution:
    def countKeyChanges(self, s: str) -> int:

        l = s.lower()
        count = 0

        for i in range(1, len(l)):
            if(l[i-1] != l[i]):
                count += 1
        
        return count