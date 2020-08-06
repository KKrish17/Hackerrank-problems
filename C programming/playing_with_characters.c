#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch,str[20],sen[100];
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    scanf("%c\n%s\n%[^\n]*c",&ch,str,sen);
    printf("%c\n%s\n%s",ch,str,sen);
    return 0;
}
