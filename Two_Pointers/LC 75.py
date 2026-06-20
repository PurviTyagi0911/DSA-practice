#Sort colors
nums=[1]
class Solution(object):
    def sortColors(self, nums):
        color_c={}
        for i in nums:
            color_c[i]=color_c.get(i,0)+1
        for n in [0,1,2]:
            if n not in color_c:
                color_c[n]=0
        for r in range(len(nums)):
            if color_c[0]>0:
                nums[r]=0
                color_c[0]-=1
            elif color_c[1]>0:
                nums[r]=1
                color_c[1]-=1
            elif color_c[2]>0:
                nums[r]=2
                color_c[2]-=1



            
        return nums        












ss=Solution()
print(ss.sortColors(nums))