#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n;
  char c;
  cin >> n >> c;
  string s;
  cin >> s;
  int score = 0;
  rep(i, n) {
    if (s[i] == 'R') score += 2;
    if (s[i] == 'B') score += 1;
  }
  bool res = false;
  if (score%3 == 0 && c == 'W') res = true;
  if (score%3 == 1 && c == 'B') res = true;
  if (score%3 == 2 && c == 'R') res = true;
  if (res) cout << "Yes" << endl;
  else cout << "No" << endl;
}
