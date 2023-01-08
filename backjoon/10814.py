n=int(input())
L1=[]
L2=[]
for x in range(n):
    a=list(input().split())
    L1.append(int(a[0]))
    L2.append(a)
L1.sort()
for x in L1:
    for y in range(n):
        if x==int(L2[y][0]):
            print(L2[y][0], L2[y][1])
            L2.pop(y)
            L2.insert(2,(-1,2))