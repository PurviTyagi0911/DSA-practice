#Non overlapping intervals
intervals = [[1,100],[2,3],[4,5]]
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals=sorted(intervals,key=lambda x:x[1])
        non_o=1
        start,end=intervals[0]
        for i in intervals[1:]:
            if i[0]>=end:
                non_o+=1
                start,end=i
        return len(intervals)-non_o,intervals
        










ss=Solution()
print(ss.eraseOverlapIntervals(intervals))
        

        