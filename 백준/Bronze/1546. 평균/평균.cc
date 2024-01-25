#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int n = 0;
	int* score;
	int max = -1;
	float* uscore;
	float uavg;
	cin >> n;
	score = new int[n];

	for (int i = 0; i < n; i++)
	{
		cin >> score[i];
	}

	for (int i = 0; i < n; i++)
	{
		if (max < score[i]) {
			max = score[i];
		}
	}

	uscore = new float[n];

	for (int i = 0; i < n; i++)
	{
		uscore[i] = 100.0*score[i] / max;
	}

	uavg = 0.0f;

	for (int i = 0; i < n; i++)
	{
		uavg += uscore[i];
	}
	uavg /= n;
	cout << uavg;

	delete[] score; //free에 해당
	return 0;
}