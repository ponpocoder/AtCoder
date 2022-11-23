#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int d, n;
  cin >> d >> n;
  vector<int> s(d,24);
  rep(i, n) {
    int l, r, h;
    cin >> l >> r >> h;
    l--; r--;
    for(int j = l; j <= r; j++) {
      chmin(s[j], h);
    }
  }
  int res = 0;
  rep(i, d) res += s[i];
  cout << res << endl;
}
