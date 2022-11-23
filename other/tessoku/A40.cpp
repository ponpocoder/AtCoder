#include <iostream>
#include <map>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int n;
  cin >> n;
  map<int, int> mp;
  rep(i, n) {
    int a;
    cin >> a;
    mp[a]++;
  }
  ll res = 0;

  for(auto x: mp) {
    int cnt = x.second;
    if (cnt >= 3) res += (ll)cnt*(cnt-2)*(cnt-1)/6;
  }
  cout << res << endl;
}
