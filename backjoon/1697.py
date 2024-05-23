#1초 x-1 or x+1 or 2*x bfs인데? 그냥?
from collections import deque
a=input().split()
x=int(a[0])
y=int(a[1])
q=deque([[x,0]])
visit=set()

while q:
    num,count=q.popleft()
    if num==y:
        print(count)
        break
    if num+1 not in visit and 0<=num+1<=100000:
        q.append([num+1,count+1])
        visit.add(num+1)
    if num-1 not in visit and 0<=num-1<=100000:
        q.append([num-1,count+1])
        visit.add(num-1)
    if 2*num not in visit and 0<=2*num<=100000:
        q.append([2*num,count+1])
        visit.add(2*num)
    