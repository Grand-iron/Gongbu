import math
n=int(input())
t=[]
count=0
for x in range(n):
    a=input().split()
    t.append(a)
    for b in a:
        if b=='5':
            p_a=x
            p_b=a.index('5')
        elif b=='2':
            y_a=x
            y_b=a.index('2')
dis=math.sqrt(((p_a-y_a)*(p_a-y_a))+((p_b-y_b)*(p_b-y_b)))
if dis<5:
    print(0)
else:
    if p_b<=y_b:
        ga=p_b
        garo=y_b
    if p_a<=y_a:
        se=p_a
        sero=y_a
    if y_a<=p_a:
        se=y_a
        sero=p_a
    if y_b<=p_b:
        ga=y_b
        garo=p_b
    for x in range(ga,garo+1):
        for y in range(se, sero+1):
            if t[y][x]=='1':
                count+=1
    if count<3:
        print(0)
    else:
        print(1)