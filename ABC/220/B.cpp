#include <iostream>
using namespace std;

int read(int k) {
  string s;
  cin >> s;
  int res = 0;
  for (char c : s) {
    res = res * k + (c - '0');
  }
  return res;
}

int main() {
  int k;
  cin >> k;
  int a = read(k);
  int b = read(k);
  cout << (long long) a*b << endl;
}
