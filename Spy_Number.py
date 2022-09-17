n=int(input())
a=1
b=0
s=0
for i in str(n):
    s=int(i)
    a=a*s
    b=b+s
if a==b:
    print("Spy Number")
else:
    print("Not Spy Number")