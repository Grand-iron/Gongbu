#include <stdio.h>
#include <stdlib.h> // rand 함수 쓰기위해 넣음
#include <time.h>  // srand값을 랜덤으로 바꾸기 위해 넣음

int main() {
	srand(time(NULL));
	main_data:   // 메인 서버 개념
		while (1) {  //오류가 나지 않는이상 계속 돌아가게 함 
			int a = rand() % 10; //a값 랜덤생성
			if (a == 1) {  //a가 1일때 오류나게 설정
				printf("오류발생 a= %d\n", a);
				break; // main_data 구문을 멈추고 밑에 복구 파트로 진입하게 함.
			}
			else{
				a = 0; //a값이 다양하게 뜨면 어지러우니 0으로 고정
				printf("이상없이 실행중 a=%d\n",a);  //서버가 돌아가는 부분을 표현
				
			}
		
		}
	int a = rand() % 10; //a 값이 오류값이 아니게 복구
	goto main_data; //복구를 마쳤으니 6번째 줄 메인서버로 보냄
}