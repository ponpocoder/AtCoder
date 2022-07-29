#include <iostream>
#include <map>
#include <vector>

using namespace std;
using ll = long long;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  map<int, int> mp;
  int n;
  cin >> n;
  vector<int> v(n);
  rep(i, n) cin >> v[i];
  ll res = 0;
  for (int i = 0; i < n; i++) {
    res += i - mp[v[i]];
    mp[v[i]]++;
  }
  cout << res << endl;

}
