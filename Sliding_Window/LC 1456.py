s='abciiidefiiiiakjbkadbak'
k=3
def maxVowels(s, k):
    l=0
    r=0
    vowels=['a','e','i','o','u']
    vowel_c=0
    for r in range(k):
        if s[r] in vowels:
            vowel_c+=1
    r=k
    max_vowel=vowel_c
    while r<len(s):
        if s[l] in vowels:
            vowel_c-=1
        l+=1
        if s[r] in vowels:
            vowel_c+=1
        max_vowel=max(vowel_c,max_vowel)
        r+=1
     
    return max_vowel
print(maxVowels(s,k))

