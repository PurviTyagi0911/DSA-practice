#bubble sort:

nums=[5,1,6,8,2,4,9]
n=0
while n<len(nums):
    for l in range(len(nums)-1):
        r=l+1
        if nums[l]>nums[r]:
            nums[l],nums[r]=nums[r],nums[l]
    n+=1

print(nums)
#T(C)=O(N^2)/ if sorted O(N), S(C)=O(1)

nums2=[1,2,3,4]
def sort(nums2):
 is_swap=False
 for i in range(len(nums2)-2,-1,-1):
  for j in range(0,i+1):
    if nums2[j]>nums2[j+1]:
        nums2[j],nums2[j+1]=nums2[j+1],nums2[j]
        is_swap=True
  if is_swap==False:
     break
 return nums2


print(sort(nums2))


