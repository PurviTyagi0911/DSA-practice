#evaluate reverse polish notation
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        for i in tokens:
            if i in '+-/*':
                a=stack.pop()
                b=stack.pop()
                if i=='+':
                    stack.append(a+b)
                elif i=='-':
                    stack.append(b-a)
                elif i=='/':
                    stack.append(int(b/a))
                elif i=='*':
                    stack.append(a*b)
            
                          
            else:
                stack.append(int(i))
            print(i,stack)
        return stack[0]
















ss=Solution()
print(ss.evalRPN(tokens))