#bubble sort:
#T(C)=O(N^2), S(C)=O(1)

nums=[5,1,6,8,2,4,9]
n=0
while n<len(nums):
    for l in range(len(nums)-1):
        r=l+1
        if nums[l]>nums[r]:
            nums[l],nums[r]=nums[r],nums[l]
    n+=1

print(nums)
nums2=[5,1,6,8,2,4,9]
for i in range(len(nums2)-2,-1,-1):
 for j in range(0,i+1):
    if nums2[j]>nums2[j+1]:
        nums2[j],nums2[j+1]=nums2[j+1],nums2[j]
print(nums2)


