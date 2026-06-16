# SUM OF 1 to N numbers using parametric recursion
summ=[]
def sumn(N):
    if N>0:
     sumn(N-1)
     print(N)
     summ.append(N)
sumn(10)
print(sum(summ))
# optimized
def sum2(sum3,i,N):
   if i>N:
      print(sum3)
      return
   sum2(sum3+i,i+1,N)
sum2(0,1,10)
#using function f(N)= N+f(N-1)
def func(N):
   if N>0:
    return func(N-1)+N
   else:
      return 0
print(func(10))
