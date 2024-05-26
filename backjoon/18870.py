def check(a, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if a[mid] < x:
            low = mid + 1
        elif a[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

n = input()  # 입력값의 개수, 사용하지 않음

# 입력값을 리스트 a로 변환
a = input().split()
# int형의 같은 리스트 b 생성
b = [int(x) for x in a]

# list(set(b))를 통해 중복 제거 후 sort()를 통해 정렬
b_sorted = sorted(list(set(b)))

# 입력값 a의 각 요소가 정렬된 리스트 b에서 몇 번째에 위치하는지를 이진 탐색을 통해 찾아 출력
for x in a:
    index = check(b_sorted, int(x))
    print(index, end=" ")

