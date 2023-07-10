class Solution(object):
    def moveZeroes(self, nums):
        a=0
        i=0
        for j in range(0,len(nums)):
            if nums[i]==0:
                a=nums.pop(i)
                nums.append(a)
            else:
                i+=1