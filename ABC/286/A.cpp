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
  int n, p, q, r, s;
  cin >> n >> p >> q >> r >> s;
  p--; q--; r--; s--;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  for(int i = p; i <= q; i++) {
    swap(a[i], a[i+r-p]);
  }
  for(int i = 0; i < n; i++) {
    if (i > 0) cout << ' ';
    cout << a[i];
  }
  cout << endl;
}
