l=0
r=0
summ=0
nums=[1,1,1,1,1,1,1,1]
target=11
while summ<target and r<len(nums):
            sum+=nums[r]
            r+=1
min_len=r-l+1
while r < (len(nums)):
            if summ<target:
               summ+=nums[r]
            while summ>=target:
                min_len=min(min_len,r-l+1)

                print(min_len,l,r,summ)
                summ-=nums[l]
                l+=1
            print(min_len,l,r,summ)

            

print( min_len)