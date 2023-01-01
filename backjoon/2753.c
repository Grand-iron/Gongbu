#include <stdio.h>

int main (void){
    int a,b,c,d;
    scanf("%d",&a);
    b=a%4;
    c=a%100;
    d=a%400;
    if(b==0 && c!=0 || d==0)
        printf("1");
    else
        printf("0");
    return 0;
}