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
  int n, m;
  cin >> n >> m;
  vector<P> a(n), b(m);
  rep(i, n) cin >> a[i].first;
  rep(i, n) cin >> a[i].second;
  rep(i, m) cin >> b[i].first;
  rep(i, m) cin >> b[i].second;
  sort(a.rbegin(), a.rend());
  sort(b.rbegin(), b.rend());
  int curr = 0;
  multiset<int> s;
  rep(i, n) {
    auto [cx, cy] = a[i];
    while (curr < m && b[curr].first >= cx) {
      s.insert(b[curr].second);
      curr++;
    }
    auto it = s.lower_bound(cy);
    if (it == s.end()) {
      cout << "No" << endl;
      return 0;
    }
    s.erase(it);
  }
  cout << "Yes" << endl;
}
