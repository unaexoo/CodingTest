#include<stdio.h>
int gcd(int num1, int num2) {
    int r = num1 % num2;

    if (r == 0) {
        return num2;
    }
    else {
        gcd(num2, r);
    }
}
int lcm(int num1, int num2) {
    return num1 * num2 / gcd(num1, num2);
}
int main()
{
    int num1, num2;
    scanf("%d %d", &num1, &num2);
    printf("%d\n", gcd(num1, num2));
    printf("%d\n", lcm(num1, num2));
}