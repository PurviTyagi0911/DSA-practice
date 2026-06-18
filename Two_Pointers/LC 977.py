nums=[-5,-3,-2,-1]
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=0
        r=len(nums)-1
        ans=[0]*len(nums)
        n=len(nums)-1
        while l<=r:
           if abs(nums[l])>abs(nums[r]):
               ans[n]=nums[l]**2
               l+=1
           else:
               ans[n]=nums[r]**2
               
               r-=1
           n-=1
               
        return ans


ss=Solution()
print(ss.sortedSquares(nums))   