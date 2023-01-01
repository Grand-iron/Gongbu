#include <stdio.h>

int main(void){
    int a,b;
    scanf("%d%d",&a,&b);
    
    if (0<a && 0<b)
        printf("1");
    else if (0<a && 0>b)
        printf("4");
    else if (0>a && 0>b)
        printf("3");
    else 
        printf("2");
    return 0;
    
}