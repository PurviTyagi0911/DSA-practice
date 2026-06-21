#permutation in string
s1="ab"
s2="a"
class Solution(object):
    def checkInclusion(self, s1, s2):
        n=len(s2)
        dict_s1={}
        for i in s1:
            dict_s1[i]=dict_s1.get(i,0)+1
        l=0
        r=len(s1)-1
        dict_s2={}
        if len(s2)<len(s1):
            return False
        else:
         for i in range(len(s1)):
            dict_s2[s2[i]]=dict_s2.get(s2[i],0)+1
         while r<n:
            if dict_s2==dict_s1:
                return True
            else:
                r+=1
                if r<n:
                 dict_s2[s2[r]]=dict_s2.get(s2[r],0)+1                
                dict_s2[s2[l]]-=1   
                if dict_s2[s2[l]]==0:
                    del dict_s2[s2[l]]
                l+=1
            print(dict_s2)
        
            
                             















ss=Solution()
print(ss.checkInclusion(s1,s2))