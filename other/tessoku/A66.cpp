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

class UnionFind{
public:
  vector<int> par;
  vector<int> rank;

  void init(int n) {
    par.resize(n);
    rep(i, n) par[i] = i;
    rank.resize(n);
    rep(i, n) rank[i] = 1;
  }

  int find(int i) {
    int p = par[i];
    while (p != par[p]) {
      par[p] = par[par[p]];
      p = par[p];
    }
    return p;
  }

  void unite(int n1, int n2) {
    int p1 = find(n1);
    int p2 = find(n2);
    if (p1 == p2) return;
    if(rank[p1] > rank[p2]) {
      rank[p1] += rank[p2];
      par[p2] = p1;
    } else {
      rank[p2] += rank[p1];
      par[p1] = p2;
    }
  }

  bool same(int n1, int n2) {
    return find(n1) == find(n2);
  }
};

int main() {
  int n, q;
  cin >> n >> q;
  UnionFind uf;
  uf.init(n);
  rep(i, q) {
    int x, u, v;
    cin >> x >> u >> v;
    u--; v--;
    if (x == 1) {
      uf.unite(u, v);
    } else {
      if (uf.same(u, v)) cout << "Yes" << endl;
      else cout << "No" << endl;
    }
  }
}
