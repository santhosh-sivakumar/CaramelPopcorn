class Solution:
    def countAsterisks(self, s: str) -> int:
        string = s.split('|')

        count = 0

        for i in range(0, len(string), 2):
            count += string[i].count('*')
        
        return count