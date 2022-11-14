#include <iostream>
#include <vector>
#include <map>

using namespace std;
using ll = long long;
using MP = map<int, vector<int>>;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int h, w, sr, sc;
  cin >> h >> w >> sr >> sc;
  int n;
  cin >> n;
  MP mpL, mpR, mpU, mpD;
  rep(i, n) {
    int r, c;
    cin >> r >> c;
    mpL[r].push_back(-c);
    mpR[r].push_back(c);
    mpU[c].push_back(-r);
    mpD[c].push_back(r);
  }

  auto init = [&](MP& mp, int s) {
    for (auto& p: mp) {
      sort(p.second.begin(), p.second.end());
      p.second.push_back(s);
    }
  };

  init(mpL, 0);
  init(mpR, w+1);
  init(mpU, 0);
  init(mpD, h+1);

  auto f = [&](MP& mp, int i, int j, int l, int w) {
    auto it = mp.find(i);
    if (it == mp.end()) return min(j+l, w-1);
    auto& is = it->second;
    int wj = *lower_bound(is.begin(), is.end(), j);
    return min(j+l, wj-1);
  };

  int q;
  cin >> q;

  rep(i, q) {
    char d; int l;
    cin >> d >> l;
    if (d == 'L') sc = -f(mpL, sr, -sc, l, 0);
    if (d == 'R') sc = f(mpR, sr, sc, l, w+1);
    if (d == 'U') sr = -f(mpU, sc, -sr, l, 0);
    if (d == 'D') sr = f(mpD, sc, sr, l, h+1);
    printf("%d %d\n", sr, sc);
  }
}
