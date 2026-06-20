#reversing an array using recursion
arr=[1,3,6,8,2,5,7,9]
def rev_arr(i,N):
    if i<=N:
        arr[i],arr[N]=arr[N],arr[i]
        rev_arr(i+1,N-1)
        return arr
print(rev_arr(5,7))
#using while loop
m=5
n=7
arr2=[1,3,6,8,2,5,7,9]
while m<=n:
        arr2[m],arr2[n]=arr2[n],arr2[m]
        m+=1
        n-=1
print(arr2)
    