a=input()
maps=[input() for x in range(a)]
방문기록=set([])
def check(x,y,count):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        # 범위 안에 있고 1인경우
        if (new_x,new_y) not in 방문기록:
            if 0 <= new_x < len(maps) and 0 <= new_y < len(maps[0]) and maps[new_x][new_y] == 1:
                count+=1
                방문기록.add((new_x,new_y))            
    return count


