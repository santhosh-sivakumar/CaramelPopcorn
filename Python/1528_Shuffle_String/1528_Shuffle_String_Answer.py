class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a = list(s)
        b = a.copy()
        for i in range(len(indices)):
            b[indices[i]] = a[i]
        return ''.join(b)    