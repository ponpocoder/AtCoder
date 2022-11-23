#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n;
  cin >> n;
  string s;
  cin >> s;
  bool res = false;
  rep(i, n-2) {
    if(s[i]==s[i+1] && s[i+1]==s[i+2]) res = true;
  }
  if (res) cout << "Yes" << endl;
  else cout << "No" << endl;
}
