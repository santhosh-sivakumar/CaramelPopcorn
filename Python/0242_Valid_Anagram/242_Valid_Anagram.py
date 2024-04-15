class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        List1 = list(s)
        List2 = list(t)

        List1.sort()
        List2.sort()

        if(List1 == List2):
            return True
        
        return False