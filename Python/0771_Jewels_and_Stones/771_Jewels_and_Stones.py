class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j, s = set(jewels), set(stones)

        u = j.intersection(s)

        count = 0
        for i in u:
            count += stones.count (i)
        
        return count