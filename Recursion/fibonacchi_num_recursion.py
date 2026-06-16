#finding 5th fibonacchi number using recursion f(x)=f(x-1)+f(x-2)
n=5
def fibonacchi_num(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
       return fibonacchi_num(n-1)+fibonacchi_num(n-2)
print(fibonacchi_num(7))
    