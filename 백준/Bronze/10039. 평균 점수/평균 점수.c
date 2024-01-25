#include<stdio.h>
int main()
{
    int student[5] = {};
    int avr = 0;
    int sum = 0;
    for (int i = 0; i < sizeof(student) / sizeof(int); i++) {
        scanf("%d", &student[i]);
        if (student[i] < 40) {
            student[i] = 40;
        }
        sum += student[i];
    }
    avr = sum / 5;
    printf("%d", avr);
}