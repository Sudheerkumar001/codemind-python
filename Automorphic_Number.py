num=int(input())
k=num*num
num=str(num)
k=str(k)
if k.endswith(num):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

