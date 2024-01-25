#include<iostream>

using namespace std;

int main() {
	int n, k;
	cin >> n >> k;

	int cnt = 0;
	int i = 0;
	for (i = 1; i < n + 1; i++) {
		if (n % i == 0) {
			cnt++;
		}
		if (cnt == k) {
			break;
		}
	}

	if (cnt == k) cout << i << endl;
	else cout << "0" << endl;
	return 0;
}