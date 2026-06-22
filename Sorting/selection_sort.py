#selection sort ascending order
nums=[1,7,8,4,5,6,9,2]
n=len(nums)
for i in range(n):
    min_indx=i
    for j in range(i+1,n):
        if nums[j]<nums[min_indx]:
            min_indx=j
    nums[i],nums[min_indx]=nums[min_indx],nums[i]
print(nums)
nums=[1,7,8,4,5,6,9,2]

#descending order
for i in range(n):
    max_indx=i
    for j in range(i+1,n):
        if nums[j]>nums[max_indx]:
            max_indx=j
    nums[i],nums[max_indx]=nums[max_indx],nums[i]
print(nums)
    