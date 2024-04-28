def solution(number, limit, power):
    answer = 0
    
    #각 번호에 약수 갯수 = 무기 공격력
    #제한수치를 넘는 공격력 = 정해진 공격력 무기 구매
    #무공 1당 1kg  철 필요 
    #언럭키 숫자블록
    
    for x in range(1,number+1):
        if x==1:
            answer+=1
        elif x==2:
            answer+=2
        else:
            count=2
            for y in range(2, int(x**(1/2)) + 1):
                if x%y==0:
                    count+=1
                    if x//y!= y: #  겹 투입 막는 중  
                        count+=1
            if count>limit:
                answer+=power
            else:
                answer+=count
                
    
    return answer