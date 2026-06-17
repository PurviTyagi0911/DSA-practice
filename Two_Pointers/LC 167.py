#Two Sum II array sorted in increasing order
numbers=[0,0,11,15]
target=0
output={}
for i in range(len(numbers)):
    needed=target-numbers[i]
    if needed in output:
        print([output[needed]+1,i+1])
    output[numbers[i]]=i
# using two pointers   
r=len(numbers)-1
l=0  
summ=0  
while l<r:
  summ=numbers[l]+numbers[r]
  if summ==target:
     print([l+1,r+1])
     break
  if summ>target:
     r-=1
  if summ<target:
     l+=1
     