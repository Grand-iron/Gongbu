n=int(input())
a=[]
for x in range(n):
    loot=list(input())
    x1=0
    y1=0
    d=4
    x2=0
    y2=0
    x3=0
    y3=0
    for y in range(len(loot)):
        if loot[y]=='L':
            d+=1
        elif loot[y]=='R':
            d-=1
        if loot[y]=='F':
            if abs(d%4)==0:
                y1+=1
            elif abs(d%4)==1:
                x1-=1
            elif abs(d%4)==2:
                y1-=1
            else:
                x1+=1
        if loot[y]=='B':
            if abs(d%4)==0:
                y1-=1
            elif abs(d%4)==1:
                x1+=1
            elif abs(d%4)==2:
                y1+=1
            else:
                x1-=1
        if x1>=x2:
            x2=x1
        if y1>=y2:
            y2=y1
        if x1<=x3:
            x3=x1
        if y1<=y3:
            y3=y1
    a.append((x2-x3)*(y2-y3))
for x in a:
    print(x)