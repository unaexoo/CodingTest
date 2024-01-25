#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(long long n) {
    // 리턴할 값은 메모리를 동적 할당해주세요.
  int count = 0;
    long long n3 = n;

    while (n3!=0)
    {
        count++;
        n3 /= 10;
    }

    int* answer = (int*)malloc(sizeof(int)*count);

    long long num1 = n;
    int num2 = 0;

    for (int i = 0; i < count; i++) {
        num2 = num1 % 10;
        num1 /= 10;
        answer[i] = num2;
    }
    return answer;
}