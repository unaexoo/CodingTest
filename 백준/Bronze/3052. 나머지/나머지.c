#include<stdio.h>
int main()
{
    int A[10] = {};
    int num[10] = {};
    int count = 0;
    int count2 = 0;

    for (int i = 0; i < 10; i++) {
        scanf("%d", &A[i]);
        num[i] = A[i] % 42;
    }

for (int i = 0; i < 10; i++) {
    count = 0;
    for (int j = i + 1; j < 10; j++) {
        if (num[i] == num[j]) {
            count++;
        }
    }
    if (count == 0) {
        count2++;
    }
}
        printf("%d", count2);
}