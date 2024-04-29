def solution(progresses, speeds):
    #각 기능 속도는 모두 다르다
    #뒤에 있는 기능은 앞에 기능이 배포될떄 함께 배포
    count=0
    count2=0
    answer=[]
    while(len(progresses)!=0):
        if progresses[0]+(speeds[0]*count)>=100:
            count2+=1
            del progresses[0]
            del speeds[0]
        else:
            if count2!=0:
                answer.append(count2)
            count+=1
            count2=0
    answer.append(count2)
    return answer