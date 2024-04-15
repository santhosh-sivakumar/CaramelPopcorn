class Solution:
    def judgeCircle(self, moves: str) -> bool:
        list = [0, 0]

        for i in moves:

            if ( i == 'U' ):
                list[0] += 1
            if ( i == 'D' ):
                list[0] -= 1
            if ( i == 'R' ):
                list[1] += 1
            if ( i == 'L' ):
                list[1] -= 1
        
        if (list == [0, 0]):
            return True
        else:
            return False