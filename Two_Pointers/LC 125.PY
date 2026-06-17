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