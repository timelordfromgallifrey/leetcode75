def isVowel(v):
    if v in ["a","e","i","o","u","A","E","I","O","U"]:
        return True
    else:
        return False

def reverseVowels(s):
    vowels=[]
    for i in s:
        if isVowel(i):
            vowels.append(i)
        else:
            pass
    
    newstring=""
    for i in range(0,len(s)):
        if isVowel(s[i]):
            newstring+=vowels.pop()
        else:
            newstring+=s[i]

    return newstring

print(reverseVowels("leetcode"))    



