#is subsequence
s='ab'
t='ab'
def check_subsequence(s,t):
        l=0
        if s==t:
                        return True
        for r in range(len(t)):
               
                if s=='':
                        return True
                if t[r]==s[l]:
                        l+=1
                if l>=len(s):
                        return True
        return False
# optimizd version of same logic
def check_subsequence2(s,t):
    l=0
    for ch in t:
            if len(s)>l and ch==s[l]:
                    l+=1
    return l==len(s)


print(check_subsequence(s,t))
print(check_subsequence2(s,t))
