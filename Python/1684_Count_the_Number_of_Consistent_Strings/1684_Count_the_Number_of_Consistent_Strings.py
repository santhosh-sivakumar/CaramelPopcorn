class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        KEY = list(allowed)
        count = flag = 0

        for i in words:
            flag = 0
            for j in i:
                if (j not in KEY):
                    flag = 1
            if (flag != 1):
                count += 1
        
        return count