#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int INF = 1001001001;

int main() {
  int n, m;
  cin >> n >> m;
  vector graph(n, vector<int>(n, INF));
  rep(i, n) graph[i][i] = 0;
  rep(i, m) {
    int a, b, c;
    cin >> a >> b >> c;
    a--; b--;
    graph[a][b] = c;
  }

  ll res = 0;
  rep(k, n) {
    rep(i, n) {
      rep(j, n) {
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
        if (graph[i][j] != INF) res += graph[i][j];
      }
    }
  }
  cout << res << endl;
}
