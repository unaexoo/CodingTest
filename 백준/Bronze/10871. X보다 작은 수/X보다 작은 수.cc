#include<iostream>
#include<vector>
using namespace std;

int main() {
	int N, X;
	cin >> N >> X;

	vector<int> v(N);

	for (int i = 0; i < N; i++) {
		cin >> v[i];
	}

	for (int i = 0; i<N; i++) {
		if (X > v[i]) {
			cout << v[i] << " ";
		}
	}
	return 0;
}