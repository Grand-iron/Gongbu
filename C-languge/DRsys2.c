#include <stdio.h>



int main() {
	int a;
main_data:
	while (1) {
		printf("몇번 학생의 학번이 궁금하신가요?");
		scanf("%d", &a);
		if (a == 1) {
			printf("1번 학생의 학번은 0001입니다.\n");
		}
		else if (a == 2) {
			printf("2번 학생의 학번은 0002입니다.\n");
		}
		else {
			printf("오류발생 ㅊ즈ㅏㅁㅇ자츠넺ㄴㅌㅋㅈㄷ(오류가 생겨서 답이 이상하게 나옴)\n");
			break;
		}
	}
	printf("복구 시스템 가동\n");
	goto main_data;
}