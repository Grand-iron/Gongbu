count=0

def solution(numbers, target):
    def target2(i,a,answer,target):
        global count
        if i==len(a):
            if answer==target:
                count+=1
            return
            
        target2(i+1,a,answer+a[i],target)
        target2(i+1,a,answer-a[i],target)
            
    target2(0,numbers,0,target)
    return count