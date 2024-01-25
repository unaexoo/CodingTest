#include<iostream>
#include<string>
using namespace std;

int main() {

    string str;
    cin >> str;

    int cnt = 0;
    int half = str.length() / 2;
    for (int i = 0; i < half; i++)
    {
        if (str[i] == str[str.length() - i - 1]) {
            cnt++;
        }
    }

    if (cnt == half) {
        cout << "1" << endl;
    }
    else {
        cout << "0" << endl;
    }
    return 0;
}