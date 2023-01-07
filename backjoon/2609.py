a,b=input().split()
c=[]
d=[]
z=0
k=0
m=1
for x in range(1,int(a)+1):
    if int(a)%x==0:
        c.append(x)
for x in range(1,int(b)+1):
    if int(b)%x==0:
        d.append(x)
for x in c:
    for y in d:
        if x==y:
            if y>=z:
                z=y
while(True):
    m+=1
    if int(a)%int(b)==0:
        k=int(a)
        break
    else:
        a=int(a)*m
        a=int(a)/(m-1)
print(z)
print(k)
