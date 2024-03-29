class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        flag = 1
        for i in range(len(s)):
            curr = s[i]

            if(curr == ')'):
                if(len(a) != 0) and(a[-1] == '(') :
                    a = a[:-1]
                else:
                    flag = 0
            elif(curr == '}'):
                if(len(a) != 0) and (a[-1] == '{'):
                    a = a[:-1]
                else:
                    flag = 0
            elif(curr == ']'):
                if(len(a) != 0) and (a[-1] == '['):
                    a = a[:-1]
                else:
                    flag = 0
            else:
                a.append(curr)
            
            if flag == 0:
                break

        if (flag == 1) and (len(a) == 0):
            return True
        else:
            return False
