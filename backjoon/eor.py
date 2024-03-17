# 이중 배열 예시
arr = [[2, 5], [1, 2], [4, 4], [2, 3]]

# 두 번째 열을 기준으로 정렬하기
# sorted() 함수 사용
sorted_arr = sorted(arr, key=lambda x: x[1])

# 혹은 arr.sort() 메소드 사용
arr.sort(key=lambda x: x[1])

# 결과 출력
print("sorted()로 정렬된 배열:", sorted_arr)
print("sort()로 정렬된 원본 배열:", arr)
print(len(arr[0]))