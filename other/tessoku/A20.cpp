#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

#define rep(i, n) for (int i = 0; i < (n); i++)

int main() {
  string s, t;
  cin >> s >> t;
  int n = s.size(), m = t.size();
  vector lcs(n+1, vector<int>(m+1));

  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
      if (s[i-1] == t[j-1]) {
        lcs[i][j] = lcs[i-1][j-1] + 1;
      } else lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1]);
    }
  }
  cout << lcs[n][m] << endl;

}
