#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)

int main() {
  int h, w, n;
  cin >> h >> w >> n;
  vector x(h+1, vector<int>(w+1));

  rep(i, n) {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    a--; b--;
    x[a][b]++;
    x[a][d]--;
    x[c][b]--;
    x[c][d]++;
  }
  rep(i,h)rep(j, w+1) x[i+1][j] += x[i][j];
  rep(i, h+1)rep(j, w) x[i][j+1] += x[i][j];
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      if (j >= 1) cout << " ";
      cout << x[i][j];
    }
    cout << endl;
  }
}
