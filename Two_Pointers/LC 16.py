#3sum Closest
nums=[-1,2,1,-4]
target=1
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums=sorted(nums)
        closest_sum=nums[0]+nums[1]+nums[2]

        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                curr_sum=nums[i]+nums[l]+nums[r]
                if abs(target-curr_sum)<abs(target-closest_sum):
                    closest_sum=curr_sum
                if curr_sum<target:
                    l+=1
                elif curr_sum>target:
                    r-=1
                else:
                    return target
                
        return closest_sum
                


ss=Solution()
print(ss.threeSumClosest(nums,target))