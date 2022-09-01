#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <numeric>
using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  vector<string> s(3);
  rep(i, 3) cin >> s[i];
  map<char, ll> mp;
  set<char> heads;
  rep(i, 3) {
    int curr = 1;
    if (i == 2) curr = -1;
    reverse(s[i].begin(), s[i].end());
    for (char c: s[i]) {
      mp[c] += curr;
      curr *= 10;
    }
    reverse(s[i].begin(), s[i].end());
    heads.insert(s[i][0]);
  }
  if (mp.size() > 10) {
    cout << "UNSOLVABLE" << endl;
    return 0;
  }
  vector<int> p(10);
  iota(p.begin(), p.end(), 0);
  do {
    int i = 0;
    ll total = 0;
    for (auto x: mp) {
      char c = x.first;
      ll curr = x.second;
      if (p[i] == 0 && heads.count(c)) total = 1e18;
      total += curr * p[i];
      i++;
    }
    if (total == 0) {
      i = 0;
      for (auto& x : mp) {
        x.second = p[i];
        i++;
      }
      rep(i, 3) {
        ll x = 0;
        for (char c : s[i]) {
          x = x*10 + mp[c];
        }
        cout << x << endl;
      }
      return 0;
    }
  } while (next_permutation(p.begin(), p.end()));
  cout << "UNSOLVABLE" << endl;
}
