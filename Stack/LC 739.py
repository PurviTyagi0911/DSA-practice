#daily temperatures
temperatures = [73,74,75,71,69,72,76,73]
class Solution(object):
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        output=[0]*n
        stack=[]
        for i in range(0,n):
          if stack==[]:
             stack.append(i)
          while stack and temperatures[i]>temperatures[stack[-1]]:
            output[stack[-1]]=i-stack[-1]
            stack.pop()
          stack.append(i)
        return output


ss=Solution()
print(ss.dailyTemperatures(temperatures))