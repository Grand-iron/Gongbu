a=input().split()
x=int(a[1])
y=int(a[0])
fried=[]
tomato=[]
answer=0
for z in range(x):
    line=[]
    n_count=0
    t=input().split()
    for q in t:
        line.append(int(q))
        if q=='1':
            fried.append([z,n_count])
        n_count+=1
    tomato.append(line)
count=len(fried)
direction=[[0,1],[0,-1],[1,0],[-1,0]]
while count!=0:
    new_fried=[]
    count=len(fried)
    answer+=1
    for z in range(count):
        new_x,new_y=fried.pop()
        for dx,dy in direction:
            if 0<=new_x+dx<len(tomato) and 0<=new_y+dy<len(tomato[0]):
                if tomato[new_x+dx][new_y+dy] == 0:
                    tomato[new_x+dx][new_y+dy]=1
                    new_fried.append([new_x+dx,new_y+dy])
    fried=new_fried


if all(0 not in l for l in tomato):
    print(answer-2)
else:
    print(-1)