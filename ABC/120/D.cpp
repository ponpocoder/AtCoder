#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stack>

using namespace std;
using ll = long long;
using P = pair<int, int>;

#define rep(i, n) for (int i = 0; i < (n); i++)

template <typename A, typename B>
ostream& operator <<(ostream& out, const pair<A, B>& a) {
  out << "(" << a.first << "," << a.second << ")";
  return out;
}

template <class T> bool chmin(T& a, T b) { return a > b ? a = b, true: false; }
template <class T> bool chmax(T& a, T b) { return a < b ? a = b, true: false; }

class Dsu {
public:
  vector<int> par;
  vector<int> rank;
  Dsu(int n): par(n), rank(n, 1) {
    for(int i = 0; i < n; i++) par[i] = i;
  }

  int find(int n) {
    int p = par[n];
    while (p != par[p]) {
      par[p] = par[par[p]];
      p = par[p];
    }
    return p;
  }

  void unite(int i, int j) {
    int p1 = find(i), p2 = find(j);
    if (p1 == p2) return;
    if (rank[p1] > rank[p2]) {
      rank[p1] += rank[p2];
      par[p2] = p1;
    } else {
      rank[p2] += rank[p1];
      par[p1] = p2;
    }
  }

  int count(int n) {
    int p = find(n);
    return rank[p];
  }

  bool connected(int i, int j) {
    int p1 = find(i), p2 = find(j);
    return p1 == p2;
  }
};

int main() {
  int n, m;
  cin >> n >> m;
  vector<P> g;
  rep(i, m) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    g.emplace_back(a, b);
  }
  vector<ll> res(m);
  ll curr = (ll)n*(n-1)/2;
  Dsu uf(n);
  for(int i = m-1; i >= 0; i--) {
    auto [a, b] = g[i];
    res[i] = curr;
    if (uf.connected(a, b)) continue;
    curr -= (ll)uf.count(a)*uf.count(b);
    uf.unite(a, b);
  }
  rep(i, m) cout << res[i] << endl;
}
