#Longest repeating character replacement
s = "AABABBA"
k = 1
class Solution(object):
    def characterReplacement(self, s, k):
         count={}
         l=0
         r=0
         win_len_max=0
         for r in range(len(s)):
              win_len=r-l+1     
              count[s[r]]=count.get(s[r],0)+1
              diff=win_len-max(count.values())
              while diff>k:
                   count[s[l]]-=1
                   if count[s[l]]==0:
                        del count[s[l]]
                   l+=1
                   win_len=r-l+1     
                   diff=win_len-max(count.values())
              if diff<=k:
                   win_len_max=max(win_len_max,r-l+1)
         return win_len_max         

ss=Solution()
print(ss.characterReplacement(s,k))