N,M=map(int,input().split())
s=0
for i in range(1,M):
    if N%i==0 and M%i==0:
        s=i
print(s)
