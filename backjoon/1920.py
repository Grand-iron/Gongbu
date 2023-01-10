import math as m
n=int(input())
a=input().split()
count=0
n2=int(input())
a2=input().split()
a.sort()
for x in a2:
    while(True):
        if int(x)<int(a[round(n/2)]):
            n=round(n/2)
        elif int(x)>int(a[round(n/2)]):
            n=round(n*1.5)
        elif int(x)==int(a[round(n/2)]):
            print(1)
            break