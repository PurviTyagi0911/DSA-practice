# K MOST FREQUENT ELEMENTS
nums=[4,1,-1,2,-1,2,3]
k=2
class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}
        output=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1    
        arr=list(freq.items())
        arr.sort(key=lambda x: x[1], reverse=True)
        for i in range(k):
               output.append(arr[i][0])
        return output
            






ss=Solution()
print(ss.topKFrequent(nums,k))