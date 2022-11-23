#include <iostream>
#include <vector>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n, k;
  cin >> n >> k;
  vector<P> a(n);
  rep(i, n) cin >> a[i].first >> a[i].second;
  int res = 0;
  for(int i=1; i<=100; i++) {
    for(int j=1; j<=100; j++) {
      int curr = 0;
      rep(l, n) {
        int x = a[l].first, y =a[l].second;
        if (x>=i && x<=i+k && y>=j && y<=j+k) curr++;
      }
      chmax(res, curr);
    }
  }
  cout << res << endl;
}
