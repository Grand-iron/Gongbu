#include <stdio.h>

int main (void){
    int a,b;
    b=1;
    scanf("%d",&a);
    while (b<10){
        printf("%d * %d = %d\n",a,b,b*a); 
        b+=1;
    } 
    return 0;           
}