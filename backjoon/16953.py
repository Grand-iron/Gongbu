def a(x, y, count):
    if x == y:
        return count
    if x > y:
        return -1
    
    # 2를 곱하는 연산과 오른쪽에 1을 추가하는 연산의 결과 중 최소값을 선택
    result = float('inf')
    temp = a(x*2, y, count+1)  # 2를 곱하는 경우
    if temp != -1:
        result = min(result, temp)
    temp = a(x*10 + 1, y, count+1)  # 오른쪽에 1을 추가하는 경우
    if temp != -1:
        result = min(result, temp)

    return result if result != float('inf') else -1

n = input().split()
a_val, b_val = int(n[0]), int(n[1])

result = a(a_val, b_val, 1)  # 초기 count를 1로 설정합니다.
print(result if result != -1 else -1)
