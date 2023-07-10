def calcVolume(h1,h2,i1,i2):
     pass

def maxArea(height):
        n=len(height)
        first=0
        last=n-1
        volumes=[]
        while first==last:
            volumes.append(calcVolume(height[first],height[last],first,last))
            if height[first]<height[last]:
                first+=1
            else:
                last-=1
        
        return max(volumes)
            

listi=[2,3,4,5,6,7]
print(max(listi))