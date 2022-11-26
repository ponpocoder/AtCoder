#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int q;
  cin >> q;
  set<int> s;
  rep(i, q) {
    int v, x;
    cin >> v >> x;
    if (v == 1) {
      s.insert(x);
    } else if (v == 2) {
      s.erase(x);
    } else {
      auto it = s.lower_bound(x);
      int res;
      if (it == s.end()) res = -1;
      else res = *it;
      cout << res << endl;
    }
  }
}
