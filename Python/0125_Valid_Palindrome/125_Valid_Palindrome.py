class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = ''
        for i in s:
            if i.isalnum():
                l = l+i
        
        l = l.lower()
        r = l[::-1]

        print(l, r, sep="\n")

        if (l == r):
            return True
        elif (len(s) == 1):
            return True
        else:
            return False

        