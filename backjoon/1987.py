a=input().split()
x=int(a[0])
y=int(a[1])
answer=1
maps=[input() for z in range(x)]
visited = [0] * 26
visited[ord(maps[0][0])-65] = 1
def check(x1,y1,count):
    global answer
    answer=max(count,answer)
    gogo=[(0,1),(0,-1),(1,0),(-1,0)] #북,남,동,서
    for z in gogo:
        dx=z[0]+x1
        dy=z[1]+y1
        if 0<=dx<len(maps) and 0<=dy<len(maps[0]):
            if visited[ord(maps[dx][dy])-65] ==0:
                visited[ord(maps[dx][dy])-65] =1
                check(dx,dy,count+1)
                visited[ord(maps[dx][dy])-65] =0

check(0,0,1)
print(answer)