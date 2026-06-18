# reverse a string
#TC =O(N), SC=O(1)
s=["h","e","l","l","o"]
class Solution(object):
    def reverseString(self, s):
        l=0
        r=len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return s
    
ss=Solution()
print(ss.reverseString(s))