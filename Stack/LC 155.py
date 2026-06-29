#min stack
class MinStack(object):

    def __init__(self):
        self.values=[]
        self.minstack=[]
        

    def push(self, val):
        self.values.append(val)
        if self.minstack==[]:
            self.minstack.append(val)
        else:
            min_value=self.minstack[-1]
            if val<min_value:
                self.minstack.append(val)
            else:
                self.minstack.append(min_value)        
        

    def pop(self):
        self.values.pop()
        self.minstack.pop()

        

    def top(self):
        return self.values[-1]
        

    def getMin(self):
        return self.minstack[-1]
    
ss=MinStack()
print(ss.push(0),ss.push(1),ss.getMin(),ss.pop(),ss.top()




)
        


