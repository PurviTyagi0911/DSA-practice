#Find all anagrams in a string
s="cbaebabacd"
p='abc'
l=0
r=0
win_c={}
p_count={}
for ch in p:
    p_count[ch]=p_count.get(ch,0)+1
for r in range(len(s)):
        win_c[s[r]]=win_c.get(s[r],0)+1
        if r-l+1>len(p):
               win_c[s[l]]-=1
               if win_c[s[l]]==0:
                  del win_c[s[l]]
               l+=1
        if win_c==p_count:
            print(l)
    
        
    
       