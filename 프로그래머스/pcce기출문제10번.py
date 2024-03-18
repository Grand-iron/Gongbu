def pandan(a):
    if a == "date":
        return 1
    elif a=="code":
        return 0
    elif a=="maximum":
        return 2
    elif a=="remain":
        return 3
    
def solution(data, ext, val_ext, sort_by):
    a1 = pandan(ext)
    a2 = pandan(sort_by)
    answer=[]
    for x in data:
        if x[a1] < val_ext:
            answer.append(x)
    answer.sort(key=lambda x: x[a2])
    return answer