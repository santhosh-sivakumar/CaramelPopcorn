class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        tmp = paths[0][0]
        flag = 1

        while( flag == 1 ):
            tmp1 = tmp
            for i in paths:
                if tmp == i[0]:
                    tmp = i[1]
            if tmp1 == tmp:
                flag = 0
        
        return tmp