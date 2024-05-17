x=input().split()
사람수=int(x[0])
연결고리갯수=int(x[1])
answer=[]
연결고리={x:[] for x in range(사람수)}

for x in range(연결고리갯수):
    q=input().split()
    연결고리[int(q[0])-1].append(int(q[1]))
    연결고리[int(q[1])-1].append(int(q[0]))

def gogo(user, freinds_num, count, past):
    if user == freinds_num: # 타겟을 찾은 경우
        return count
    if len(연결고리[user])!=0:
        min_count = float('inf') # 최소 카운트를 매우 큰 값으로 초기화
        for x in 연결고리[user]:
            if x not in past:
                new_past = past + [user] # 현재 노드를 포함한 새로운 경로 리스트
                temp_count = gogo(x, freinds_num, count+1, new_past)
                if temp_count is not None: # 탐색에 성공했다면
                    min_count = min(min_count, temp_count)
        if min_count != float('inf'):
            return min_count
    return float('inf') # 탐색에 실패한 경우 큰 값을 반환

for x in range(사람수):
    a=float('inf') # 최소값을 찾기 위해 초기값을 매우 큰 값으로 설정
    b=[]
    for y in range(사람수):
        if x != y: # 자기 자신으로의 경로는 제외
            temp = gogo(x, y, 0, b)
            a=min(a, temp)
    answer.append(a)
print(min(answer))
