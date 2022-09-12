n=int(input())
s=0
while n:
    k=n%10
    s=s+k*k
    n=n//10
    if s>9 and n==0:
        n=s
        s=0
if s==7 or s==1:
    print(True)
else:
    print(False)