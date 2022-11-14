#include <iostream>
#include <vector>

using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)

int main() {
  int h, w;
  cin >> h >> w;
  vector<string> s(h);
  rep(i, h) cin >> s[i];
  int res = 0;
  for(int i = 0; i < h-1; i++) {
    for (int j = 0; j < w-1; j++) {
      int cnt = 0;
      rep(x, 2) rep(y, 2) if (s[i+x][j+y] == '#') cnt ++;
      if (cnt == 1 || cnt == 3) res++;
    }
  }
  cout << res << endl;
}
