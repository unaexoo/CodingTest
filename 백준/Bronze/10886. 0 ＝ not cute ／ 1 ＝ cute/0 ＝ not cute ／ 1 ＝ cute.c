#include<stdio.h>
int main()
{
	int N;
	scanf("%d", &N);
	int arr[100];
	int count = 0;
	int count2 = 0;
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
		if (arr[i] == 0) {
			count++;
		}
		else if (arr[i] == 1) {
			count2++;
		}
	}
	if (count > count2) {
		printf("Junhee is not cute!");
	}
	else
	{
		printf("Junhee is cute!");
	}
}