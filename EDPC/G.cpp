#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

void dfs(vector<vector<int>> &graph, vector<int> &dp, int i) {
  if (dp[i] != -1) return;
  int l = 0;
  for (auto dest: graph[i]) {
    if (dp[dest] == -1) dfs(graph, dp, dest);
    l = max(l, 1+dp[dest]);
  }
  dp[i] = l;
  return;
}

int main() {
  int n, m;
  cin >> n >> m;
  vector<vector<int>> graph(n);

  rep(i, m) {
    int x, y;
    cin >> x >> y;
    x--;
    y--;
    graph[x].push_back(y);
  }

  vector<int> dp(n, -1);
  rep(i, n) if(dp[i] == -1) dfs(graph, dp, i);
  int res = 0;
  rep(i, n) res = max(res, dp[i]);
  cout << res << endl;
}
