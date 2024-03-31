class Solution:
    def maxBottlesDrunk(self, full: int, exchange: int) -> int:
        count = empty = 0
        
        while(full > 0):
            count += full
            empty += full
            full = 0
            
            while (empty > 0) and (empty >= exchange):
                full += 1
                empty -= exchange
                exchange += 1
        
        return count