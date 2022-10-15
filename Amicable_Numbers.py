n=int(input())
m=int(input())
c=0
d=0
for i in range(1,n):
    if n%i==0:
        c+=i
for i in range(1,m):
    if m%i==0:
        d+=i
if(c==m and d==n):
    print("Amicable")
else:
    print("Not Amicable")