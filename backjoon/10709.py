h,w=input().split()
asdf=[]
for x in range(int(h)):
    a=list(input())
    asd=[]
    for y in a:
        if y!='c':
            asd.append(-1)
        elif y=='c':
            asd.append(0)
    for y in range(1,int(w)):
        if asd[y-1]>=0:
            if asd[y]!=0:
                asd[y]=asd[y-1]+1
            else:
                asd[y]=0
    asdf.append(asd)

for x in range(int(h)):
    for y in range(int(w)):
        print(asdf[x][y],end=' ')
    print()