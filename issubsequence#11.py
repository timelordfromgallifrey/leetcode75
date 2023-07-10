class Solution(object):
    def isSubsequence(self, s, t):
        j=-1
        flag=0
        if s=="":
            return True
        if len(t)<len(s):
            return False

        for i in range(0,len(s)):
            while True:
                j+=1
                if s[i]==t[j]:
                    if i==len(s)-1:
                        return True
                    if j>len(t)-2:
                        return False
                    flag=1
                    break
                if j>len(t)-2:
                    return False
            if flag==0:
                return False
                    
