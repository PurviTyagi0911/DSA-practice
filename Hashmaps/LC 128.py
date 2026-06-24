#longest consecutive sequence
nums = [6,7,8,9]
class Solution(object):
    def longestConsecutive(self, nums):
        store=set()
        max_count=0
        count=0
        for r in nums:
            store.add(r)
        for r in store:
            if r-1 not in store:
                count=0
                while r+count in store:
                    count+=1                  
            max_count=max(max_count,count)
                     
        return max_count










ss=Solution()
print(ss.longestConsecutive(nums))