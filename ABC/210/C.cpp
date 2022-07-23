#include <iostream>
#include <map>
#include <vector>

using namespace std;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, k;
  cin >> n >> k;

  vector<int> c(n);
  rep(i, n) cin >> c[i];

  map<int, int> mp;
  int res = 0;
  int curr = 0;
  for (int i = 0; i < n; i++) {
    if (mp[c[i]] == 0) curr++;
    mp[c[i]]++;
    if (i >= k) {
      mp[c[i-k]]--;
      if (mp[c[i-k]] == 0) curr--;
    }
    res = max(res, curr);
  }
  cout << res << endl;
}
