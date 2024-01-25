#include<stdio.h>
int main()
{
	int n = 0;
	scanf("%d", &n);

	int num = 0;
	int mul = 1;

	while (n != 0) {
		num = n;
		mul *= num;
		n -= 1;
	}
	printf("%d", mul);
}