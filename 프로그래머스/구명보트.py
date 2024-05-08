def solution(people, limit):
    answer = 0         #한 배에 최대 2명이기에 가장 무거운 사람을 많이 엮어서 내보내는걸 우선
    l_cursor=0         #가장 무거운 + 작은 사람을 확인하여 limit을 확인
    r_cursor=-1        #[   80     ,   70  ,   50  ,     50    ]
    남은수=len(people)  # l_cursor       남은 수            r_cursor
    people.sort()
    while True:
        if 남은수>1:
            if people[r_cursor]+people[l_cursor]<=limit:
                r_cursor-=1
                l_cursor+=1
                남은수-=2
            else:
                r_cursor-=1
                남은수-=1
        elif 남은수==1:
            answer+=1
            break
        else:
            break
        answer+=1
    return answer