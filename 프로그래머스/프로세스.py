def solution(priorities, location):
    answer = 0
    a= [x for x in range(len(priorities))]
    while(len(priorities)!=0):
        a1=a.pop(0)
        a2=priorities.pop(0)
        if len(priorities)==0:
            if a1==location:
                answer+=1
                return answer
        elif a2<max(priorities):
            priorities.append(a2)
            a.append(a1)
        elif a1==location:
            answer+=1
            return answer
        else:
            answer+=1
