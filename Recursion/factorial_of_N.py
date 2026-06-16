#factorial of a number using recursion
#f(N)=f(N-1)*N
def f(N):
    if N>0:
        return f(N-1)*N
    elif N==0:
        return 1
print(f(8))