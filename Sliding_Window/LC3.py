#longest substring without repeating characters
s='dvdf'
def longest_str(s):
        l=0
        r=0
        strr=set()
        count=0
        for r in range(len(s)):
            while s[r] in strr:
                  strr.remove(s[l])
                  l+=1
            if s[r] not in strr:
              strr.add(s[r])
            count=max(count,r-l+1)
            print(count,s[r])
        return count
        
print(longest_str(s))