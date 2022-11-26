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
  int q;
  cin >> q;
  map<string, int> mp;
  rep(i, q) {
    int v;
    cin >> v;
    if (v == 1) {
      string x;
      int y;
      cin >> x >> y;
      mp[x] = y;
    } else {
      string x;
      cin >> x;
      cout << mp[x] << endl;
    }
  }
}
