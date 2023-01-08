import sys
n=int(sys.stdin.readline())
a=[0]*10001
for x in range(n):
    c=int(sys.stdin.readline())
    a[c]+=1
for y in range(10001):
    if a[y]!=0:
        for z in range(a[y]):
            print(y)