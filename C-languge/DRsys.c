#include <stdio.h>
#include <stdlib.h> // rand 함수 쓰기위해 넣음
#include <time.h>  // srand값을 랜덤으로 바꾸기 위해 넣음
#include <windows.h>
// 학생 자료 구조체 선언
void loading(void);
int menu(void);
int s_who(void);
char s_name(int num);     //이름 반환 (매개변수는 26번줄에서 who 함수를 통해 받을 몇번 학생인지에 대한 정보)
char s_class(int num);    //학과 반환 (위와 동일)
int s_num(int num);       //학번 반환 (위와 동일)
int s_age(int num);       //나이 반환 (위와 동일)

int main() {
	//여기다가 학생 자료 넣기.
onebone:
	while (1) {
		int changer, who;
		int (*a[4])(int); //[s_name, s_class, s_num, s_age]; 왼쪽꺼 넣을거임
		srand(time(NULL));
		loading();
		changer = menu();
		if (changer < 0 || changer>6)
			printf("잘못된 범위의 값을 입력하셨습니다.");
		else if (changer < 5) {
			who = s_who();
			a[changer](who);   //이름 학과 학번 나이 출력해주는 함수포인터 배열
		}
		else if (changer == 6)
			goto finish;  //프로그램 끝내기
		else
			break;  //while식 넘어 복구 식으로 이동.
			
	}
	//데이터 파일 복구 식 넣기
	goto onebone; //복구 끝난뒤 다시 onnbone으로 이동.
finish:
	printf("사용해주셔서 감사합니다.");
	return 0;
}

void loading(void) {  //로딩창
	int i;
	for (i = 0; i < 100; i++) {
		printf("\r프로그램 로딩중 %02d", i);
		Sleep(10);
	}
	printf("\r프로그램 로딩 완료!\n");
}

int menu(void) {
	int a;
	printf("**************************************\n");
	printf("찾고 싶으신 데이터를 숫자로 입력해주세요. (오류날 확률 50%)\n");
	printf("0. 학생이름\n");
	printf("1. 학과\n");
	printf("2. 학번\n");
	printf("3. 학년\n");
	printf("4. 나이\n");
	printf("5. 오류발생시 복구 프로그램\n");
	printf("6. 종료\n");
	printf("**************************************\n");
	scanf("%d", &a);
	return a;
}
int s_who(void) {         
	int a;
	printf("몇번 학생의 정보를 보고 싶으십니까? 1~3");
	scanf("%d", &a);
	return a;
}
char s_name(int num);        //구조체로 만들어진 데이터 중 name,class,num,age를 출력해주는 함수 4가지 만들예정.
char s_class(int num);
int s_num(int num);
int s_age(int num);