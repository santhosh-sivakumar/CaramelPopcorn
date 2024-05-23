class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        OUT = 0
        columnTitle = columnTitle[::-1]

        for i in range( len(columnTitle) ):
            OUT += ( ord( columnTitle[i] ) - 64) * (26 ** i)

        return OUT