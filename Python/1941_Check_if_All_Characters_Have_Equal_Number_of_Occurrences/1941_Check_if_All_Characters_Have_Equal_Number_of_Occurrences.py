class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char = set(s)
        freq = []

        for i in char:
            freq.append( s.count(i) )
        
        for i in range( len(freq) - 1 ):
            if freq[i] != freq[i + 1]:
                return False
        return True