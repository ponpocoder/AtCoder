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

class dsu {
public:
  vector<int> par;
  vector<int> rank;

  void init(int n) {
    par.resize(n);
    rep(i, n) par[i] = i;
    rank.resize(n);
    rep(i, n) rank[i] = 1;
  }

  int find(int n) {
    int p = par[n];
    while(p != par[p]) {
      par[p] = par[par[p]];
      p = par[p];
    }
    return p;
  }

  void unite(int n1, int n2) {
    int p1 = find(n1);
    int p2 = find(n2);
    if (p1 == p2) return;
    if (rank[p1] > rank[p2]) {
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
  int n, m;
  cin >> n >> m;
  vector<tuple<int, int, int>> edges;
  dsu uf;
  uf.init(n);

  rep(i, m) {
    int a, b, c;
    cin >> a >> b >> c;
    a--; b--;
    edges.push_back(make_tuple(c, a, b));
  }
  sort(edges.begin(), edges.end());
  int res = 0;
  rep(i, m) {
    int c = get<0>(edges[i]);
    int b = get<1>(edges[i]);
    int a = get<2>(edges[i]);
    if (uf.same(a, b)) continue;
    uf.unite(a, b);
    res += c;
  }

  cout << res << endl;
}
