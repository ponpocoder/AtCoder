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

  bool connected(int i, int j) {
    int p1 = find(i), p2 = find(j);
    return p1 == p2;
  }
};
