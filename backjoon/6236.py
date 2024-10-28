n,m=input().split()

L=[]
for x in range(int(n)):
    L.append(int(input()))

left =max(L)
right=sum(L)

while left<=right:
    mid=(left+right)//2
    total=0
    count=1
    for x in L:
        total+=x
        if total>mid:
            total=0
            count+=1
    
    if count>int(m):
        left=mid+1
    else:
        right=mid-1

print(mid)