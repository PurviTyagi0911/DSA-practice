#Insert INterval
intervals = [[1,5]]
newInterval = [2,3]
class Solution(object):
    def insert(self, intervals, newInterval):
        answer=[]
        start_n=newInterval[0]
        end_n=newInterval[1]
        for curr in intervals:
            if start_n > curr[1]:
                answer.append(curr)
            elif curr[0]>end_n:
                answer.append(newInterval)
                newInterval=curr
            elif start_n<=curr[1] or end_n<=curr[1] :
                newInterval=[min(curr[0],start_n),max(end_n,curr[1])]
                start_n=newInterval[0]
                end_n=newInterval[1]
        answer.append(newInterval)
        return answer




                

















ss=Solution()
print(ss.insert(intervals,newInterval))