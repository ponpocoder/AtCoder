#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int h, w;
  cin >> h >> w;
  vector x(h, vector<int>(w));
  vector s(h+1, vector<int>(w+1));

  rep(i, h) rep(j, w) {
    cin >> x[i][j];
  }
  rep(i, h)rep(j, w) s[i+1][j+1] = x[i][j];
  rep(i, h+1)rep(j, w) s[i][j+1] += s[i][j];
  rep(i, h)rep(j, w+1) s[i+1][j] += s[i][j];

  int q;
  cin >> q;
  rep(i, q) {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    a--; b--;
    int curr = s[c][d];
    curr -= s[a][d];
    curr -= s[c][b];
    curr += s[a][b];
    cout << curr << endl;
  }
}
