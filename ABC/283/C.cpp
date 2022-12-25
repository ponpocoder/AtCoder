#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <typename A, typename B>
ostream& operator <<(ostream& out, const pair<A, B>& a) {
  out << "(" << a.first << "," << a.second << ")";
  return out;
}

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  string s;
  cin >> s;
  int cnt = 0, zero = 0;
  for(char c: s) {
    if (c == '0') {
      if (zero == 0) zero++;
      else { cnt++; zero = 0;}
    } else {
      cnt++;
      if(zero == 1) {cnt++; zero = 0;}
    }
  }
  if (zero) cnt++;
  cout << cnt << endl;
}
