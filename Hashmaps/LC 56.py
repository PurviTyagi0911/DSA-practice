#Merge Intervals
intervals = [[1,8],[0,6]]
class Solution(object):
    def merge(self, intervals):
        intervals=sorted(intervals)
        output=[]
        start=intervals[0][0]
        end=intervals[0][1]
        output.append(intervals[0])
        for s in intervals:
                if s[0] in range(start,end+1):
                    output.pop(-1)
                    end=max(s[1],end)
                    output.append([start,end])
                    print('extend')
                else:
                     start=s[0]
                     end=s[1]
                     output.append([start,end])
                
        return output  
            
        






ss=Solution()
print(ss.merge(intervals))