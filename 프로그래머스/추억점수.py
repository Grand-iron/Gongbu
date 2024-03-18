def solution(name, yearning, photo):
    answer=[]
    for x in photo:
        count=0
        for y in x:
            if y in name:
                count+=yearning[name.index(y)]
        answer.append(count)
    return answer