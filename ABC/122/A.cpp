#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  char b;
  cin >> b;
  if (b == 'A') cout << 'T' << endl;
  if (b == 'C') cout << 'G' << endl;
  if (b == 'G') cout << 'C' << endl;
  if (b == 'T') cout << 'A' << endl;
}
