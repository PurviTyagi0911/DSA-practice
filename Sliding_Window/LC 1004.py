# max num subarray

#using nested loops t(c)=o(N^2)
arr=[1,1,1,0,0,0,1,1,1,1,0]
i=0
j=0
k=2
maxi=0

for i in range(0,len(arr)):
    zeroes=0
    for j in range(i,len(arr)):
        if arr[j]==0:
            zeroes+=1
        if zeroes>k:
            break
        maxi=max(maxi,j-i+1)
print(maxi)

#using sliding window T(c)=O(2N)
left=0
right=0
maxii=0
zero=0
k=2
while right<len(arr):
    if arr[right]==0:
        zero+=1
    if zero>k:
        if arr[left]==0:
            zero-=1
        left+=1 
    if zero<=k:       
      maxii=max(maxii,right-left+1)
    print(left,right,maxii,zero)
    right+=1
print(maxii)

   