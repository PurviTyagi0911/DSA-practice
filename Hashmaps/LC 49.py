#group anagrams
strs = ["eat","tea","tan","ate","nat","bat"]
class Solution(object):
    def groupAnagrams(self, strs):
        output=[]
        store={}
        for s in strs:
            strr=sorted(s)
            strr=''.join(strr)
            if strr not in store:
                store[strr]=[]
                store[strr].append(s)

            else:
                store[strr].append(s)

        for o in store:
            output.append(store[o])
        return output

                










ss=Solution()
print(ss.groupAnagrams(strs))