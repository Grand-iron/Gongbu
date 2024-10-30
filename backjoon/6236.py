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
        if total + x > mid:
            total = x  # 새로운 그룹 시작
            count += 1
        else:
            total += x  # 현재 그룹에 x 추가
    
    if count>int(m):
        left=mid+1
    else:
        right=mid-1
        answer=mid

print(answer)