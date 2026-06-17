#Valid Palindrome
s = "A man, a pla8n, a can8al: Panama"
strr=[]
def check_palindrome(s):
  for i in s:
    if ord(i)>64 and ord(i)<91:
        i=i.lower()

    if ord(i)>96 and ord(i)<123:
        strr.append(i)
    elif ord(i)>47 and ord(i)<58:
        strr.append(i)
       
  r=len(strr)-1
  l=0

  while r>=l:
    if strr[r]==strr[l]:
        l+=1
        r-=1
    else:
        return False
        break
  return True
print(check_palindrome(s))
# using isallnum space complexity O(1) from O(n)
def check_p(s):
   r=len(s)-1
   l=0
   while l < r:

            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

   return True
print(check_p(s))