n = int(input())
 
c = [] 
ans = [] 
for x in range(n):
    a, b = map(int, input().split())
    c.append((a, b)) 
 
for x in range(n):
    count = 0
    for y in range(n):
        if c[x][0] < c[y][0] and c[x][1] < c[y][1]: 
            count += 1 
    ans.append(count + 1) 
for d in ans:
    print(d,end=" ")
