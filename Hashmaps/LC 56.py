#Merge Intervals
intervals = [[1,8],[7,10]]
class Solution(object):
    def merge(self, intervals):
        intervals=sorted(intervals)
        output=[]
        start,end=intervals[0]

        for curr_start, curr_end in intervals[1:]:
               if curr_start<=end:
                    end=max(curr_end,end)
               else:
                 output.append([start,end])
                 start,end=curr_start,curr_end
        output.append([start,end])
                    
                    

               
                
        return output  
            
        






ss=Solution()
print(ss.merge(intervals))