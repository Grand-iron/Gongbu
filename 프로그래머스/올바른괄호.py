def solution(s):
    a=[]
    for x in (s):
        if x == "(":               # 열린괄호면 추가 
            a.append(x)
        else:
            if len(a)==0:         # 닫힌괄호인데 (가 큐에 없으면 False 있으면 ( 한개 삭제
                return False
            else:
                a.pop()
    if len(a)==0:                #최종적으로 길이가 0이면 True 0이 아니면 (ex:"("가 남아있는 경우) False 
        return True
    else:
        return False