#include<iostream>
#include<algorithm>
#include<array>
using namespace std;

int main() {
	array<int, 5>arr;
	int sum = 0;

	for (int i = 0; i < 5; i++) {
		cin >> arr[i];
		sum += arr[i];
	}

	sort(arr.begin(), arr.end());
	cout << sum / 5 << endl<< arr[2] << endl;

	return 0;
}