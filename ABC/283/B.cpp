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
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i, n) cin >> a[i];
  int q;
  cin >> q;
  rep(i, q) {
    int v, k;
    cin >> v >> k;
    k--;
    if (v == 1) {
      int x;
      cin  >> x;
      a[k] = x;
    } else {
      cout << a[k] << endl;
    }
  }
}
