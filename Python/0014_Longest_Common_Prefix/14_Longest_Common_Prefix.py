class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        OUT= ''
        strs = sorted(strs, key = len)

        for i in range( len(strs[0]) ):
            flag = 1
            for j in strs:
                if strs[0][i] != j[i]:
                    flag = 0
            
            if flag:
                OUT += strs[0][i]
            else:
                break
        
        
        return OUT