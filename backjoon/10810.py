a=input().split()
li=[]
for x in range(int(a[0])):
    li.append(0)
for x in range(int(a[1])):
    b=input().split()
    c=int(b[1])-int(b[0])
    li[int(b[0])-1]=int(b[2])
    for y in range(c):
        li[int(b[0])+y]=int(b[2])

for x in li:
    print(x,end=" ")