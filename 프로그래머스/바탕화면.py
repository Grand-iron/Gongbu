def solution(wallpaper):
    countx1=99
    county1=99
    countx2=-1
    county2=-1
    county=0
    countx=0
    for x in wallpaper: 
        county=0
        if "#" in x and countx1==99:
            countx1=countx
        countx+=1
        if "#" in x and countx>=countx2:
            countx2=countx
        for y in x:
            if y=="#" and county<=county1:
                county1=county
            county+=1
            if y=="#" and county>=county2:
                county2=county
    answer = [countx1,county1,countx2,county2]
    return answer