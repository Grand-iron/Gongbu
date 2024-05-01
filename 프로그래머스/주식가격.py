def solution(prices):
    length = len(prices)
    answer = [0] * length  # 각 시점의 가격이 떨어지지 않은 시간을 저장할 배열
    stack = []  # 이전 가격들의 인덱스를 저장할 스택
    
    for i, price in enumerate(prices):
        # 스택이 비어 있지 않고, 현재 가격이 스택의 top에 있는 가격보다 작으면
        # 스택의 top 가격은 현재 가격에 의해 떨어진 것.
        while stack and price < prices[stack[-1]]:
            top = stack.pop()
            answer[top] = i - top  # 떨어진 시점 계산
        stack.append(i)
    
    # 스택에 남아 있는 인덱스는 가격이 떨어지지 않고 마지막까지 간 것들
    while stack:
        top = stack.pop()
        answer[top] = length - 1 - top
    
    return answer
