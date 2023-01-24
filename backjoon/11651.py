n=int(input())
z=[]
for x in range(n):
    k=[]
    a=input().split()
    a.reverse()
    k.append(int(a[0]))
    k.append(int(a[1]))
    z.append(k)
z.sort()
for x in range(n):
    print(z[x][1],z[x][0])