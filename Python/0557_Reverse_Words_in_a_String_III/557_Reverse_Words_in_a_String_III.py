class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.split()

        for i in range(len(s1)):
            s1[i] = s1[i][::-1]

        return ' '.join(s1)