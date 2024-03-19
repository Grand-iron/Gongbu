def solution(players, callings):
    a={er:int(num) for num,er in enumerate(players)}
    for x in callings:
        q= a[x] #q에는 호명된 이름의 원래 번호 저장
        
        a[x]-=1
        a[players[q-1]]+=1
        
        players[q]=players[q-1]
        players[q-1]=x
    return players