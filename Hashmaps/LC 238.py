#product of array except self
nums = [5,9,2,-9,-9,-7,-8,7,-9,10]
class Solution(object):
    def productExceptSelf(self, nums):
        dict_product={}
        for i in nums:
            dict_product[i]=dict_product.get(i,0)+1
        answer=[]
        for l in nums:
            dict_product[l]-=1
            product=1
            for r in dict_product:
                 product*=(r**dict_product[r])

            answer.append(product)
            dict_product[l]+=1

        return answer

        











ss=Solution()
print(ss.productExceptSelf(nums))