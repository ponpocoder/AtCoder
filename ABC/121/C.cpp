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
  int n, m;
  cin >> n >> m;
  vector<P> a(n);
  rep(i, n) cin >> a[i].first >> a[i].second;
  sort(a.begin(), a.end());
  int cnt = 0;
  ll res = 0;
  for(int i=0; i<n; i++) {
    if(cnt == m) break;
    int remain = min(a[i].second, m-cnt);
    res += (ll)remain*a[i].first;
    cnt += remain;
  }
  cout << res << endl;
}
