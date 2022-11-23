#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <class T> bool chmin(T& a, T& b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T& b) { return a < b ? a = b, true: false; }

int main() {
  int q;
  cin >> q;
  deque<string> a;
  rep(i, q) {
    int v;
    cin >> v;
    if (v == 1) {
      string x;
      cin >> x;
      a.push_back(x);
    } else if (v == 2) {
      string res = a.front();
      cout << res << endl;
    } else a.pop_front();
  }
}
