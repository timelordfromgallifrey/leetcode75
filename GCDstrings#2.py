class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:        
        if len(str1) < len(str2):    #to capture which one is the smallest. if true, str2 will be made str1, else str2 remains str2, in both cases, str2 remains smaller
            str1, str2 = str2, str1
        
        L, S = len(str1), len(str2)
        
        for i in range(S, 0, -1):
            if (L/i) == int(L/i) and (S/i) == int(S/i):
                c = str2[:i]
                if c*int(L/i) == str1 and c*int(S/i) == str2: 
                    return c
                
        return ""