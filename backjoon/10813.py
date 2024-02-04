a=input().split()
li=[]
for x in range(int(a[0])):
    li.append(x+1)

for x in range(int(a[1])):
    b=input().split()
    c=li[int(b[0])-1]

    li[int(b[0])-1]=li[int(b[1])-1]
    li[int(b[1])-1]=c

for x in li:
    print(x,end=" ")