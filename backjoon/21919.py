n=int(input())
a=input().split()
sosu=[]
for x in range(n):
    if not a[x] in sosu:
        for y in range(2,int(a[x])):
            if int(a[x])%y==0:
                break
        else:
            sosu.append(int(a[x]))
if len(sosu)==0:
    print(-1)
else:
    ans=1
    for i in len(sosu):
        ans*=sosu[i]
    print(ans)