#include <iostream>
#include <vector>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n;
  cin >> n;
  vector<P> a(n);
  rep(i, n) {
    cin >> a[i].second >> a[i].first;
  }
  sort(a.begin(), a.end());

  int curr = 0, res = 0;
  rep(i, n) {
    if (a[i].second >= curr) {
      res += 1;
      curr = a[i].first;
    }
  }
  cout << res << endl;
}
