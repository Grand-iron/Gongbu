a=[]
for x in range(int(input())):
    a.append(input())

for x in range(len(a)):
    print(a[x][0],end="")
    count=len(a[x])
    print(a[x][count-1])