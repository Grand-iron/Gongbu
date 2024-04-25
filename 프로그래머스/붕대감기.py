def solution(bandage, health, attacks):
    # [시전 시간, 초당 회복량, 추가 회복량] 형태 [공격 시간, 피해량]
    count=0
    time=[]
    for x in attacks:
        time.append(x[0])
    
    max_hp=health
    for x in range(time[len(time)-1]):
        if x+1 in time:              #데미지 공식
            health-=attacks[time.index(x+1)][1]
            count=0
        else:
            if health <max_hp :
                health+=bandage[1]
                count+=1
                if count%bandage[0]==0:
                    health+=bandage[2]
                    count=0
        if health > max_hp:
            health=max_hp
            
        if health<=0:
            return -1
    return health