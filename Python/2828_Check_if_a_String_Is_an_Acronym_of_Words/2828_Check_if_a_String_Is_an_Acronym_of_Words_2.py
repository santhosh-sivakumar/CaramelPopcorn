class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        concat = ''

        for i in words:
            concat += i[0]

        if (concat == s):
            return True
        else:
            return False