class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        List = [i[0] for i in words]
        return ''.join(List) == s