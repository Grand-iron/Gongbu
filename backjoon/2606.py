#연결된 컴퓨터 정보를 각 딕셔너리에 담아 재귀함수를 통해 연결된 값들을 전부 지우며 확인한다.
컴터수=int(input())  
연결고리갯수=int(input())

#재귀함수를 통해 바이러스 체크
def virus(num):
    while 컴퓨터링크[num-1]: 
        hack_num=컴퓨터링크[num-1].pop()
        virus(hack_num)
        answer[hack_num-1]=1

#answer배열에서 바이러스 검출시 1로 값을 변경
answer=[0 for x in range(컴터수)]
컴퓨터링크={x:[] for x in range(컴터수)}

for x in range(연결고리갯수):
    q=input().split()
    #양방향 링크이기에 각 키값에 밸류값으로 넣기
    컴퓨터링크[int(q[0])-1].append(int(q[1]))
    컴퓨터링크[int(q[1])-1].append(int(q[0]))

#재귀함수 실행
virus(1)
#1번 컴퓨터 정보 빼기
answer.pop(0)
#감연된 정보 = 1 값 출력
print(answer.count(1))