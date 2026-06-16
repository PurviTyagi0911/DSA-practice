nums = [1,12,-5,-6,50,3]
k = 4
r=0
l=0
summ=0
while r<k:
            summ+=nums[r]
            r+=1
r-=1
max_sum=summ
while r<len(nums)-1:
            r+=1
            summ+=nums[r]
            summ-=nums[l]
            l+=1
            max_sum=max(max_sum,summ)
            print("sum =", summ, "max =", max_sum)
            
print(max_sum/k)