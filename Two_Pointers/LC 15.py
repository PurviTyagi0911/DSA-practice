#3sum
from collections import Counter
nums= [-2,0,1,1,2]
class Solution(object):
    def threeSum(self, nums):
        nums=sorted(nums)
        output=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            l=i+1
            r=len(nums)-1
            sum=0
            while l<r:
                sum=nums[l]+nums[r]
                if sum<target:
                    l+=1
                elif sum>target:
                    r-=1
                else:
                    output.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1        
        return output
ss=Solution()
print(ss.threeSum(nums))