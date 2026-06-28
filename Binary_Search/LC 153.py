#find minimum in rotated sorted array
#T(C)=O(log(n))
nums = [5,6,7,1,2,3,4]
class Solution(object):
    def findMin(self,nums):
           n=len(nums)
           left=0
           right=n-1
           mid=n//2
          
           for mid in range(len(nums)):
              
               if nums[left]>nums[right]:
                    if nums[mid]>nums[right]:
                         left=mid+1
                         mid=(right-left+1)//2
                    else:
                         left+=1
                         mid=(right-left+1)//2

               else:
                    return nums[left]
                
                         
               







ss=Solution()
print(ss.findMin(nums))