#checking a palindrome(str) using recursion
s="NITIN"
def check_palindrome(i,N):
    if i<N:
        if s[i]!=s[N]:
            return False
        return check_palindrome(i+1,N-1)
    return True
print(check_palindrome(0,len(s)-1))

#using while loop
def check_palindrome2(n,m): 
 while n<m:
    if s[n]!=s[m]:
        return False
    n+=1
    m-=1
 return True
print(check_palindrome2(0,len(s)-1))
    
