def kidsWithCandies(self, candies, extraCandies):
        n=len(candies)
        isgreatest=[]
        
        for i in range(0,n):
            candies[i]+=extraCandies
            if candies[i]==max(candies):
                isgreatest.append(True)
            else:
                isgreatest.append(False)
            candies[i]-=extraCandies
        
        return isgreatest