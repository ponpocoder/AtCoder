#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  int n, m;
  cin >> n >> m;
  vector<int> cnt(n);
  int ac = 0;
  int wa = 0;
  rep(i, m) {
    int p; string s;
    cin >> p >> s;
    p--;
    if (cnt[p] != -1) {
      if (s == "AC") {
        ac++;
        wa += cnt[p];
        cnt[p] = -1;
      } else {
        cnt[p]++;
      }
    }
  }
  cout << ac << " " << wa << endl;
}
