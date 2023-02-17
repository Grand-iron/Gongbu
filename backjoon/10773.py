import sys
n=int(sys.stdin.readline())
a=[]
ans=0
for x in range(n):
    k=int(sys.stdin.readline())
    if k!=0:
        a.append(k)
    else:
        a.pop()
for x in a:
    ans+=x
print(ans)