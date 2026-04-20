import math
n=int(input("enter a number:"))
root=math.isqrt(n)
if root*root==n:
    print("perfect square")
else:
    print("not a perfect square")


n=int(input("enter a number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
        print("perfect numbe")
else:
        print("not a perfect number")
        
