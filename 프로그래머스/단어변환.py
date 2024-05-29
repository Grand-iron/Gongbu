from collections import deque

def isOneLetterDifferent(word1, word2):
    # 두 단어 간 한 글자만 다른지 여부를 확인
    difference = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            difference += 1
        if difference > 1:
            return False
    return difference == 1

def solution(begin, target, words):
    if target not in words:
        return 0  # 목표 단어가 words 리스트에 없으면 변환 불가능
    
    queue = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
    visited = set([begin])  # 방문한 단어 집합
    
    while queue:
        current_word, step = queue.popleft()
        if current_word == target:
            return step  # 목표 단어에 도달했으면 현재까지의 변환 횟수를 반환
        
        for word in words:
            if word not in visited and isOneLetterDifferent(current_word, word):
                visited.add(word)
                queue.append((word, step + 1))  # 변환 횟수를 1 증가시키고 큐에 추가
    
    return 0  # 모든 경우를 탐색했으나 목표 단어로의 변환이 불가능한 경우

