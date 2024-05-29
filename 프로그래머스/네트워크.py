b_list=[]
def check(computers,i,count):
    for b,x in enumerate(computers[i]):
        if x==1 and b_list[b]==0:
            b_list[b]=count
            check(computers,x,count)
    

def solution(n, computers):
    global b_list
    for x in range(n):
        b_list.append(0) 
    i=0
    count=1
    while 0 in b_list:
        if b_list[i]==0:
            b_list[i]=count
            check(computers,i,count)
            count+=1
        i+=1
        
    answer = len(set(b_list))
    return answer