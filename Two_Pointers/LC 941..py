#Valid Mountain Array
arr=[0,1,2,3,2,1,0,1,2,1,0]
class Solution(object):
    def validMountainArray(self, arr):
        r=len(arr)-1
        l=0
        n=len(arr)
        if n==1:
            return False
        while l<n-1 and arr[l]<arr[l+1] :
            l+=1
        while arr[r]<arr[r-1]:
            r-=1
        if r==l and l!=0 and r!=len(arr)-1:
            return True
        else:
            return False










ss=Solution()
print(ss.validMountainArray(arr))