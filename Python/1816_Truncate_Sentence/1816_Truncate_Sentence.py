class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s1 = s.split()
        s1 = s1[:k]

        return ' '.join(s1)