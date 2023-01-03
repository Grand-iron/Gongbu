#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,x;
    int a;
    int b;
    scanf("%d %d\n",&n, &x);
        for(b=0; b<n; b++)
        {
            scanf("%d", &a);
            if (a < x)
            printf("%d ", a);
        }
}