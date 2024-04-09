class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        while(tickets[k] != 0):
        
            if(tickets[0] == 0):
                tickets.pop(0)
                k -= 1
            else:
                tmp = tickets[0]
                time += 1
                k -= 1
                tickets.pop(0)
                tickets.append(tmp - 1)
        
            if(k == -1):
                k = len(tickets) - 1
        
        return time