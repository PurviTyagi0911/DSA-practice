#max water storage
height=[1,8,6,2,5,4,8,3,7]
class Solution(object):
    def maxArea(self, height):
        area=0
        l=0
        r=len(height)-1
        while l<r:
            length=r-l
            tall=min(height[l],height[r])
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
            area=max(area,length*tall)
        return area





ss=Solution()
print(ss.maxArea(height))
