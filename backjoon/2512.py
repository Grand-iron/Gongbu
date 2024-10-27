a=int(input())

n=input().split()
m=int(input())

left=0
right=max(n)
    
while left <=right:
    total=0
    mid=(left+right)//2
    for x in n:
        if int(x)>mid:
            total+=mid
        else:
            total+=int(x)
    if total>m:
        right=mid-1
    else:
        left=mid+1
print(right)