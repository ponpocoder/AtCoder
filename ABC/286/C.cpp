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
  int n, a, b;
  cin >> n >> a >> b;
  string s;
  cin >> s;
  s += s;
  ll res = 1e18;
  for(int i = 0; i < n; i++) {
    ll curr = (ll)a * i;
    for(int j = 0; j < n/2; j++) {
      int l = i + j;
      int r = i + n - 1 - j;
      if (s[l] != s[r]) curr += (ll)b;
    }
    res = min(res, curr);
  }
  cout << res << endl;
}
