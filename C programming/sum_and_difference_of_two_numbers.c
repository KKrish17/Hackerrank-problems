#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int m,n;
    float a,b;
	scanf("%d %d\n%f %f",&m,&n,&a,&b);
    printf("%d %d\n%.1f %.1f",m+n,m-n,a+b,a-b);
    return 0;
}
