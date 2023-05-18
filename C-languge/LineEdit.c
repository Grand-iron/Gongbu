#include <stdio.h> //대부분은 나름 안보며 적었지만 방식과 과정은 ppt의 통일했기에 따로 주석설명은 하지 않겠습니다.
#include <stdlib.h>
#include <string.h> //strstr() 및 몇가지를 쓰기위해 사용

#define MAX_CHAR_PER_LINE 1000
typedef struct Line {
  char str[MAX_CHAR_PER_LINE];
} Element;

typedef struct LinkedNode {
  Element data;
  struct LinkedNode* link;
} Node;

Node *head=NULL; 
void display (FILE *fp);
void init_list() { head = NULL; }
int is_empty() { return head == NULL; }
Node* get_entry(int pos);
int size() ;
void replace(int pos, Element val);
Node* find(Element e);
void insert_next(Node *prev, Node *node);
void insert(int pos, Element val);
Node* remove_next(Node *prev);
void delete(int pos);
void my_fflush(){while (getchar() !='\n');}
int papago(char Command); //메뉴의 b 부분 번역 파트
int reset(){head=NULL;}  //메뉴의 m 부분 파트트

int main(){
  char command,choice;
  int pos;
  Element line;
  FILE *fp;
  do {
    printf("[메뉴선택] i-입력, d-삭제, r-변경, b-번역, p-출력, l-파일읽기, s-저장,m= 리셋, q-종료=>");
    command = getchar();
    switch (command) {
      case 'i':
        printf(" 입력행 번호: ");
        scanf("%d", &pos);
        printf(" 입력행 내용: ");
        my_fflush(); // 입력 버퍼(키보드)에서 ‘\n’을 비움
        fgets(line.str, MAX_CHAR_PER_LINE, stdin);
        insert(pos, line);
        break;
      case 'd':
        printf(" 삭제행 번호: ");
        scanf("%d", &pos);
        delete(pos);
        break;
      case 'r':
        printf(" 변경행 번호: ");
        scanf("%d", &pos);
        printf(" 변경행 내용: ");
        my_fflush();
        fgets(line.str, MAX_CHAR_PER_LINE, stdin);
        replace(pos, line);
        break;
      case 'l':
        fp= fopen("Test.txt","r");
        if (fp != NULL) {
          while (fgets(line.str, MAX_CHAR_PER_LINE, fp))
            insert(size(), line);
            fclose(fp);
          }
        break;
      case 'b': 
        printf("전체 번역-a,개별 번역-s =>"); //선택지 제공 및 scanf를 이용하여 받았다
        scanf(" %c", &choice);
        papago(choice); //매개변수로 선택지에 대한 값을 넣어준다.
        break;
      case 'm':
        reset();
        break;
      case 's':
        fp = fopen("Test.txt", "w");
        if (fp != NULL) {
          display(fp);
          fclose(fp);
        }
      case 'p': display(stdout);
        }
      my_fflush();
      } while (command != 'q');
  return(0);
}

void display(FILE *fp){
  int i = 0;
  Node *p;
  for (p=head; p!=NULL;p=p->link,i++){
    fprintf(stderr,"%3d: ",i );
    fprintf(fp,"%s",p->data.str);
  }
  printf("\n");
}

Node* get_entry(int pos){
  Node* p = head;
  int i;
  for (i = 0; i<pos; i++, p = p->link)
    if (p == NULL)
      return NULL;
  return p; 
}

int size(){
  Node* p;
  int count = 0;
  for (p = head; p != NULL; p = p->link)
    count++;
  return count;
}

void replace( int pos, Element e){
  Node* node = get_entry(pos);
  if (node != NULL)
    node->data = e;
}

void insert_next(Node *prev, Node *node){
if (node != NULL) {
  node->link = prev->link;
  prev->link = node;
}}

void insert(int pos, Element val){
  Node *new_node,
  *prev;
  new_node = (Node*)malloc(sizeof(Node));
  new_node->data = val;
  new_node->link = NULL;
  if (pos == 0) {
    new_node->link = head;
    head = new_node;
  }
  else {
    prev = get_entry(pos - 1);
    if (prev != NULL)
      insert_next(prev, new_node);
    else free(new_node);
}
}

Node* remove_next(Node *prev){
  Node* removed = prev->link;
  if (removed != NULL)
    prev->link = removed->link;
  return removed;
}

void delete(int pos){
  Node* prev, *removed;
  if (pos == 0 && is_empty() == 0){ 
    removed = head;
    head = head->link;
    free(removed);
  }
  else {
    prev = get_entry(pos - 1);
    if (prev != NULL) {
      removed = remove_next(prev);
      free(removed);
    }
  }
}

int papago(char Command){
  FILE *fp;                              //번역된 글이 담긴 텍스트 파일을 이용한다. 마치 백과사전에서 영단어 뜻을 검색하듯
  int i = 0,count =0,No=0;               //i= for문을 위해 , count = papago.txt에 번역이 없는 영단어를 위해, No는 번역 값을 출력할때 라인 번호를 보여주기 위해
  Node *p;
  char word[MAX_CHAR_PER_LINE];          //입력된 데이터의 값을 문자열로 치환하여 쓰기 위한 변수
  char buffer[MAX_CHAR_PER_LINE];        //텍스트 파일을 한줄씩 읽어 담을 변수
  if ((fp = fopen("papago.txt", "r"))==NULL){  //만약 열리지 않을경우 쓰일 조건
    fprintf(stderr,"papago 파일을 열 수 없습니다. \n");
    return 0;
  }
  if (Command == 'a'){  //전체 번역의 경우 모든 노드의 data의 str값을 긁어와 word에 담고 '\n'을 없앤다.
    for (p=head; p!=NULL;p=p->link,i++){
      strcpy(word,p->data.str);
      for (i=0;word[i]!=0;i++){
        if (word[i]=='\n'){
          word[i]=0;
        }
      }
      while(fgets(buffer, 256,fp)){ //파일을 한줄씩 불러와 그 줄에 word 변수의 값이 있는지 확인하고 있다면 출력과 No를 달며 Count를 1올린다.
        if(strstr(buffer, word) != NULL){
          count+=1;
          printf("%3d: %s",No,buffer);
        }
      }
      if (count==0) //만약 위에서 한번도 조건문을 통과하지 못했을 경우 count값이 0이기에 위와 같이 출력한다.
        printf("%3d: %s의 번역 자료가 없습니다\n",No,word);
      count=0;
      No++;
      rewind( fp); //첫번째 문자를 확인한뒤 다시 papago.txt를 읽어야 다음 문자도 확인이 가능하기에 사용했다.
    }
    fclose(fp);  //닫는 부분과 int로 쓰여진 함수기에 return 0;
    return 0;
  }
  else if (Command == 's'){  //원하는 단어를 입력받아 papago.txt에 있는지 확인한다 방식은 위와 동일
    printf("번역하고자 하는 단어를 입력해주세요 :");
    scanf("%s", &word);
    while(fgets(buffer, 256,fp)){
        if(strstr(buffer, word) != NULL){
          count+=1;
          printf("%s",buffer);
        }
      }
      if (count==0)
        printf("%s의 번역 자료가 없습니다\n",word);
      count=0;
  return 0;
  }
}