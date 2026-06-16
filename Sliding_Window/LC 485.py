l=0
maxi=0
nums=[0]
#nums=[0,0,0]
#nums=[1,0,1,1,0,1]
#nums=[1,1,0,1,1,1]
for r in range(len(nums)):
            if nums[r]==0 and r+1<len(nums) :
                l=r+1
            if nums[r]==1:
             maxi=max(maxi,r-l+1)
print(maxi)