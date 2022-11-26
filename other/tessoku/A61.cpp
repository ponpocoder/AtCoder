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
  vector g(n+1, vector<int>(0));
  rep(i, m) {
    int a, b;
    cin >> a >> b;
    g[a].push_back(b);
    g[b].push_back(a);
  }
  for(int i=1; i <=n; i++) {
    cout << i << ": {";
    rep(j, (int)g[i].size()) {
      if (j>0) cout << ", ";
      cout << g[i][j];
    }
    cout << "}" << endl;
  }
}
