#include<stdio.h>
int main()
{
    int A = 0, B = 0, C = 0;
    scanf("%d %d %d", &A, &B, &C);
    int mul = A * B * C;
    int mul2 = 0;
    int array[10] = {};
    while (mul != 0)
    {
        mul2=mul% 10;
        array[mul2]++;
        mul /= 10;
    }
    for (int i = 0; i < 10; i++) {
        printf("%d\n", array[i]);
    }
    return 0;
}