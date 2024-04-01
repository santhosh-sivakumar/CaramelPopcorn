class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1], [1,1]]

        if(numRows > 2):   
            for i in range(1, numRows-1):
                next = [1]
                for j in range(len(out[i])-1):
                    next.append(out[i][j] + out[i][j+1])
                next.append(1)
                out.append(next)

        return out[:numRows]