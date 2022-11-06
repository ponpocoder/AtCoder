#include <iostream>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int h, w;
const int x[4] = {0, 0, 1, -1};
const int y[4] = {1, -1, 0, 0};
string g[1000001];
bool visited[1000001];

bool dfs(int r, int c, int d) {
  visited[r*w+c] = true;
  for (int i = 0; i < 4; i++) {
    int nr = r+x[i], nc = c+y[i];
    if (nr < 0 || nr >= h || nc < 0 || nc >= w || g[nr][nc] == '#') continue;
    if (g[nr][nc] == 'S' && d >= 4) return true;
    if (visited[nr*w+nc]) continue;
    if (dfs(nr, nc, d+1)) return true;
  }
  return false;
}

int main() {
  cin >> h >> w;
  rep(i, h) cin >> g[i];
  int sr = -1;
  int sc = -1;
  rep(i, h)rep(j, w) if (g[i][j] == 'S') {sr = i; sc = j;}
  cout << (dfs(sr, sc, 0) ? "Yes" : "No") << endl;
}
