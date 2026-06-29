#find minimum in rotated sorted array
#T(C)=O(log(n))
nums = [9,8,7,0,1,2,3,4,5]
class Solution(object):
    def findMin(self,nums):
           n=len(nums)
           left=0
           right=n-1
           while left<right:
               mid=(right+left)//2      
               if nums[mid]>nums[right]:
                    left=mid+1
               else:
                    right=mid
               print(nums)
           return nums[left]
                         
               







ss=Solution()
print(ss.findMin(nums))