#next greater element I
nums1 = [4,1,2]
nums2 = [1,3,4,2]
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        d = {}

        for n in nums2:
            while stack and n > stack[-1]:
                d[stack.pop()] = n

            stack.append(n)
        print(d)

        while stack:
            d[stack.pop()] = -1
        print(d)

        ans = []

        for num in nums1:
            ans.append(d[num])

        return ans
    

ss=Solution()
print(ss.nextGreaterElement(nums1,nums2))