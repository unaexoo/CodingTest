#include<iostream>

using namespace std;

int main() {

	string S;
	int i;
	cin >> S >> i;

	for (int j = 0; j < S.length(); j++) {
		if (j + 1 == i) {
			cout << S[j] << endl;
			return 0;
		}
	}
	return 0;
}