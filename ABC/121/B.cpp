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
  int n, m, c;
  cin >> n >> m >> c;
  vector<int> b(m);
  rep(i, m) cin >> b[i];
  int res = 0;
  rep(i, n) {
    int curr = c;
    rep(j, m) {
      int a;
      cin >> a;
      curr += a*b[j];
    }
    if (curr>0) res++;
  }
  cout << res << endl;
}
