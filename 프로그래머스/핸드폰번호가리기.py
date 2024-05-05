def solution(phone_number):
    answer=""
    for x in range(len(phone_number)-4):
        answer+="*"
    for x in range(len(phone_number)-4,len(phone_number)):
        answer+=phone_number[x]
    
    return answer