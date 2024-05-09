# def solution(number, k):
#     answer = ""                  #1        9          2     4 
#     n=0                          #n                   k
#     남은수=k  #빼야할수            #제거수 범위중큰수
                                 
#                                  #answer 문자열에 범위중큰수 추가 + 남은수 -= 제거수
    
#                                  #                    n     k
    
#     while 남은수>0:
#         if 남은수==len(number)-len(answer):
#             return answer
#         범위중큰수=max(number[n:k+1])
#         제거수=number.index(범위중큰수,n,k+1)-n
#         answer+=범위중큰수
#         n=n+제거수+1
#         남은수=남은수-제거수
#         k=n+남은수
#     answer+=number[n:]
#     return answer

def solution(number, k):
    stack = []  # 숫자들을 저장할 스택
    n = 0  # 현재 숫자의 위치
    남은수 = k

    for num in number:
        # 스택에 숫자가 있고, 남은수가 0보다 크며, 현재 스택의 마지막 숫자가 현재 숫자보다 작은 경우
        while stack and 남은수 > 0 and stack[-1] < num:
            stack.pop()  # 스택의 마지막 숫자를 제거
            남은수 -= 1  # 제거해야 할 숫자의 개수를 감소
        stack.append(num)  # 현재 숫자를 스택에 추가

    # 만약 남은수가 0보다 크면, 그만큼의 수를 스택 끝에서 제거
    stack = stack[:-남은수] if 남은수 > 0 else stack
    
    return ''.join(stack)
