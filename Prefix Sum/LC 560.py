#subarray sum equals to K
nums =[1,-1,0]
k = 0
class Solution(object):
    def subarraySum(self,nums,k):
        n=len(nums)
        summ=[0]*n
        summ[0]=nums[0]
        for i in range(1,n):
            summ[i]=summ[i-1]+nums[i]
        prefix={0:1}
        print(summ)
        count=0
        for i in range(len(summ)):
            if summ[i]-k in prefix:
                count+=prefix[summ[i]-k]
            
            prefix[summ[i]] = prefix.get(summ[i], 0) + 1
            print(prefix)
        return count


















ss=Solution()
print(ss.subarraySum(nums,k))