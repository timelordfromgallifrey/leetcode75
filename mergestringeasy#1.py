def mergeAlternately(word1, word2):
        newword=""
        wordlength=0
        if len(word1)<len(word2):
                wordlength=len(word1)
        else:
                wordlength=len(word2)
        j=0
        for i in range(0,wordlength*2,2):
                newword+=word1[j]
                newword+=word2[j]
                j+=1
        
        if wordlength==len(word1):
                for j in range(j,len(word2)):
                        newword+=word2[j]
        else:
                for j in range(j,len(word1)):
                        newword+=word1[j]
                

        return newword   


                                