#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

struct Edge {
  int to, id;
};

vector<vector<Edge>> graph;
vector<int> res;


void dfs(int curr, int p, int x) {
  int k = 1;
  rep(i, int(graph[curr].size())) {
    int dest = graph[curr][i].to, id = graph[curr][i].id;
    if (dest == p) continue;
    if (k == x) k++;
    res[id] = k;
    dfs(dest, curr, k);
    k++;
  }
}

int main() {
  int n;
  cin >> n;
  graph.resize(n);
  res.resize(n);
  rep(i, n-1) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    graph[a].push_back((Edge){b, i});
    graph[b].push_back((Edge){a, i});
  }
  dfs(0, -1, -1);
  int cnt = 0;
  rep(i, n-1) cnt = max(cnt, int(graph[i].size()));
  cout << cnt << endl;
  rep(i, n-1) cout << res[i] << endl;
}
