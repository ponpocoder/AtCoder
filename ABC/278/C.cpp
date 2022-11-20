#include <iostream>
#include <vector>
#include <set>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n, q;
  cin >> n >> q;
  set<P> s;
  rep(i, q) {
    int t, a, b;
    cin >> t >> a >> b;
    if (t == 1) s.emplace(a, b);
    if (t == 2) s.erase(P(a, b));
    if (t == 3) {
      if (s.count(P(a,b)) && s.count((P(b,a)))) {
        cout << "Yes" << endl;
      } else {
        cout << "No" << endl;
      }
    }
  }
}
