x=input().split()
사람수=int(x[0])
연결고리갯수=int(x[1])
answer=[]
연결고리={x:[] for x in range(사람수)}

for x in range(연결고리갯수):
    q=input().split()
    연결고리[int(q[0])-1].append(int(q[1]))
    연결고리[int(q[1])-1].append(int(q[0]))

def gogo(user, friends_num, count, past):
    # 사용자 번호를 인덱스로 변환
    user_index = user - 1
    friends_index = friends_num - 1

    if len(연결고리[user_index]) != 0:  # 연결된 친구가 있는지 확인
        if user_index == friends_index:  # 자기 자신을 찾은 경우
            return count
        min_count = float('inf')
        for x in 연결고리[user_index]:
            if x not in past:
                new_past = past + [user]  # 현재 사용자를 경로에 추가 (사용자 번호는 그대로 사용)
                # x는 연결고리에서 바로 사용하는 값이므로, x+1을 해서 원래의 사용자 번호로 복구
                result = gogo(x + 1, friends_num, count + 1, new_past)
                if result is not None:
                    min_count = min(min_count, result)
        if min_count == float('inf'):  # 친구를 찾지 못한 경우
            return None
        else:
            return min_count

for x in range(사람수):
    a = float('inf')  # 초기값을 무한대로 설정
    b = []
    for y in range(사람수):
        result = gogo(x, y, 0, b)
        if result is not None:  # 결과가 None이 아닌 경우에만 비교
            a = min(a, result)
    answer.append(a)

print(min(answer))
