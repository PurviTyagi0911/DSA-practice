#product of array except self
nums = [1,2,3,4]
class Solution(object):
     def productExceptSelf(self, nums):
       answer=[]
       p_l=1
       p_r=1
       n=len(nums)
       r=n
       right=[]
       for r in range(n-1,-1,-1):
            if r==n-1:
               p_r=1
            else:
              p_r*=nums[r+1]
            right.append(p_r)
       for t in range(n):
           if t==0:
            p_l=1
           else:
            p_l*=nums[t-1]
           summ=p_l*right[n-1-t]
           answer.append(summ)
                  
       return answer
        







ss=Solution()
print(ss.productExceptSelf(nums))