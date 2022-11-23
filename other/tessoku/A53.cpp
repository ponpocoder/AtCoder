#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int q;
  cin >> q;
  priority_queue<int, vector<int>, greater<int>> a;
  rep(i, q) {
    int v;
    cin >> v;
    if (v == 1) {
      int x;
      cin >> x;
      a.push(x);
    } else if (v == 2) {
      int res = a.top();
      cout << res << endl;
    } else a.pop();
  }
}
