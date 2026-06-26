#product of array except self
nums = [1,2,3,4]
class Solution(object):
     def productExceptSelf(self, nums):
       n=len(nums)
       
       answer=[1]*n
       left_product=1
       right_product=1
       right=[]
       for l in range(n):
          answer[l]=left_product
          left_product*=nums[l]
          
       for r in range(n-1,-1,-1):
            answer[r]*=right_product
            right_product*=nums[r]
                  
       return answer
        







ss=Solution()
print(ss.productExceptSelf(nums))