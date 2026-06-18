#remove duplicates of a sorted array
nums=[0,1,1,1,2,2,3,4]
class Solution(object):
    def removeDuplicates(self, nums):
        s=0
        f=1
        while f<len(nums):
          if nums[s]==nums[f]:
            f+=1
          else:
             s+=1
             nums[s]=nums[f]
        return s+1,nums

        
        
ss=Solution()
print(ss.removeDuplicates(nums))
